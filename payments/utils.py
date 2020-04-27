import requests
import sys
import hmac
import hashlib
from django.utils.timezone import now, localdate, datetime
from datetime import timedelta
import pytz

from event_manager.settings import RAZORPAY_KEY, RAZORPAY_MID, RAZORPAY_SECRET, TIME_ZONE
from .models import Subscription

BASE_URL = "https://api.razorpay.com/v1"
auth = (RAZORPAY_KEY, RAZORPAY_SECRET)
tz = pytz.timezone(TIME_ZONE)


def create_order(amount):
    res = requests.post(
        f"{BASE_URL}/orders",
        json={
            "amount": amount * 100,
            "currency": "INR",
            "receipt": "receipt",
            "payment_capture": 1,
        },
        auth=auth,
    ).json()
    if "error" in res:
        return False, res["error"]
    return True, res["id"]


def compare_string(expected_str, actual_str):
    if len(expected_str) != len(actual_str):
        return False
    result = 0
    for x, y in zip(expected_str, actual_str):
        result |= ord(x) ^ ord(y)
    return result == 0


def is_signature_safe(parameters):
    order_id = str(parameters["razorpay_order_id"])
    payment_id = str(parameters["razorpay_payment_id"])
    razorpay_signature = str(parameters["razorpay_signature"])
    msg = "{}|{}".format(order_id, payment_id)

    if sys.version_info[0] == 3:  # pragma: no cover
        key = bytes(RAZORPAY_SECRET, "utf-8")
        body = bytes(msg, "utf-8")

    dig = hmac.new(key=key, msg=body, digestmod=hashlib.sha256)

    generated_signature = dig.hexdigest()

    if sys.version_info[0:3] < (2, 7, 7):
        result = compare_string(generated_signature, razorpay_signature)
    else:
        result = hmac.compare_digest(generated_signature, razorpay_signature)

    if not result:
        return False
    return True


def get_order(order_id):
    res = requests.get(f"{BASE_URL}/orders/{order_id}/payments", auth=auth).json()
    return res["items"]


def handle_order(order, query):
    model = order.order._meta.model_name
    if model == 'propack':
        today = localdate(now())
        pack = Subscription(user=order.order_id.user, start_date=today)
        if query['meta_data']['pack_type'] == 'monthly':
            pack.end_date = today + timedelta(days=30)
        else:
            pack.end_date = today + timedelta(days=365)
        pack.save()


def create_subscription(plan_id, total_count, user, meta_data):
    if meta_data is None:
        meta_data = dict()
    res = requests.post(f'{BASE_URL}/subscriptions', json=dict(
        plan_id=plan_id,
        total_count=total_count,
        customer_notify=0,
        **meta_data
    ), auth=auth).json()
    if "error" in res:
        return False, res["error"]
    sub = Subscription.objects.create(sub_id=res['id'], sub_type=meta_data['notes[sub_type]'],
                                      payment_url=res['short_url'], user=user)
    return True, sub


def update_subscription(sub, start_date, end_date):
    sub.start_date = datetime.fromtimestamp(start_date, tz).date()
    sub.end_date = datetime.fromtimestamp(end_date, tz).date()
    sub.save()


def renew_subscription(sub_id, sub_type, start_date, end_date):
    sub = Subscription.objects.filter(sub_id=sub_id, sub_type=sub_type).latest('end_date')
    sub.pk = None
    update_subscription(sub, start_date, end_date)

