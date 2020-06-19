from django.db.models import Q, Sum, F
from django.db.models.functions import Coalesce

from utils.base_manager import BaseManager


class ProductManager(BaseManager):
	def get_products(self, user, **kwargs):
		return self.select_related('category').filter(
			Q(user__username=user) | Q(resell_product__sellers__user__username=user)
		).annotate(total_stock=Coalesce(Sum('sizes__stock'), 0) + F('stock')).order_by('-total_stock').\
			filter(**kwargs)

	def get_resell_products(self, user):
		return self.select_related('category').filter(resell_product__sellers__user__username=user).\
			annotate(total_stock=Coalesce(Sum('sizes__stock'), 0) + F('stock')).order_by('-total_stock')