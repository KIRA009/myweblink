from uuid import uuid4
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.timezone import localdate, now
from django.contrib.postgres.fields import ArrayField
from json import loads
from django.db.utils import IntegrityError

from utils.base_model_mixin import AutoCreatedUpdatedMixin
from .managers import UserManager, LinkManager
from utils.exceptions import AccessDenied


class User(AbstractBaseUser, PermissionsMixin, AutoCreatedUpdatedMixin):
    email = models.EmailField(max_length=256, unique=True)
    is_staff = models.BooleanField(default=False)
    phone = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=256)
    secret = models.UUIDField(default=uuid4)
    is_validated = models.BooleanField(default=False)
    username = models.TextField(unique=True)
    profile_pic = models.URLField(default="", null=True, blank=True)
    background_color = models.TextField(default=None, null=True, blank=True)
    background_image = models.URLField(default=None, null=True, blank=True)
    college = models.ForeignKey(
        "College",
        related_name="students",
        on_delete=models.CASCADE,
        to_field="name",
        null=True,
    )
    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def user_type(self):
        from payments.models import Subscription
        today = localdate(now())
        return 'pro' if self.subscriptions.filter(sub_type=Subscription.PROPACK, start_date__lte=today,
                                                  end_date__gte=today).exists() else 'normal'

    class Encoding(AutoCreatedUpdatedMixin.Encoding):
        exclude_fields = AutoCreatedUpdatedMixin.Encoding.exclude_fields.copy()
        for i in ["password", "last_login", "is_superuser", "is_staff", "secret"]:
            exclude_fields.append(i)

        process_fields = AutoCreatedUpdatedMixin.Encoding.process_fields.copy()
        process_fields.update(**dict(
            links=lambda x: [_.detail() for _ in x.links.all()],
            user_type=lambda x: x.user_type
        ))

    def change_secret(self):
        self.secret = uuid4()
        self.save()

    def change_password(self, password):
        self.set_password(password)
        self.change_secret()

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        self.username = self.username.lower()
        try:
            super().save(*args, **kwargs)
        except IntegrityError as e:
            raise AccessDenied(str(e))


class College(AutoCreatedUpdatedMixin):
    name = models.TextField(unique=True)
    address = models.TextField()
    state = models.TextField()
    has_college_email = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Link(AutoCreatedUpdatedMixin):
    title = models.TextField(default="")
    url = models.URLField(default="", null=True, blank=True)
    visible = models.BooleanField(default=False)
    index = models.IntegerField(default=0)
    icon = models.URLField(default="", null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="links"
    )

    objects = LinkManager()


class ProModeFeature(AutoCreatedUpdatedMixin):
    header_icon = models.URLField(default="", null=True, blank=True)
    header_text = models.TextField(default="", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feature")


class ProPack(AutoCreatedUpdatedMixin):
    INR = 'INR'
    USD = 'USD'
    CURRENCIES = (
        (INR, '₹'),
        (USD, '$')
    )
    MONTHLY = 'monthly'
    YEARLY = 'yearly'
    TYPES = (
        (MONTHLY, 'Monthly pack'),
        (YEARLY, 'Yearly pack'),
    )
    price = models.IntegerField(default=300)
    plan_id = models.TextField(blank=True, default='')
    period = models.CharField(max_length=256, default=MONTHLY, blank=True, choices=TYPES)
    currency = models.TextField(choices=CURRENCIES, default=INR)
    features = ArrayField(models.TextField(blank=True), default=list, blank=True)

    def save(self, *args, **kwargs):
        from payments.utils import get_plan, create_plan
        if self.plan_id:
            error, plan = get_plan(self.plan_id)
            if error:
                return
            if plan['item']['amount'] != 100 * self.price or plan['period'] != self.period:
                self.plan_id = create_plan(self)['id']
        super(ProPack, self).save()

    class Encoding(AutoCreatedUpdatedMixin.Encoding):
        process_fields = AutoCreatedUpdatedMixin.Encoding.process_fields.copy()
        process_fields.update(**{
            'features': lambda x: loads(x)
        })
