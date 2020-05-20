from django.views import View
from django.shortcuts import redirect

from payments.models import Order
from payments.utils import create_order_form, create_order, send_text_update
from payments.validators import update_order_schema
from utils.exceptions import AccessDenied
from event_manager.settings import PAYMENT_CANCEL_URL, PAYMENT_CALLBACK_URL
from utils.tasks import handle_order


class OrderView(View):
    def get(self, request):
        return dict(orders=request.User.orders.all().detail())

    # @create_order_schema
    def post(self, request):
        data = request.json
        user_details = data['user_details']
        order_id, user = create_order(data['cod_items'], 'cod', user_details)
        if order_id:
            handle_order(dict(
                payload=dict(
                    order=dict(
                        entity=dict(id=order_id)
                    ),
                    payment=dict(
                        entity=dict(
                            order_id=order_id
                        )
                    )
                )
            ))
        order_id, user = create_order(data['online_items'], 'online', user_details)
        if order_id:
            return dict(form=create_order_form(order_id, user))
        return dict(message="Order created")


class UpdateSoldProductsView(View):
    @update_order_schema
    def post(self, request):
        data = request.json
        order = Order.objects.get(id=data['item_id'])
        seller = order.items.first().order.user
        if seller != request.User:
            raise AccessDenied()
        order.status = data['status']
        order.save()
        send_text_update(order)
        if order.cod and order.status == Order.DELIVERED:
            percent = seller.commission['cod']['percent'] * 0.01
            extra = seller.commission['cod']['extra']
            for item in order.items.all():
                seller.amount -= int(percent * item.order.disc_price) + extra
                item.order.stock -= int(item.meta_data['quantity'])
                item.order.save()
            seller.save()
        return dict(item=item.detail())


class GetSoldProductsView(View):
    def get(self, request):
        page_no = int(request.GET.get('pageNo', 1))
        status = str(request.GET.get('delivered', 'true'))
        query = Order.objects.get_sold_products(request.User)
        if status == 'true':
            query = query.filter(status=Order.DELIVERED)
        else:
            query = query.exclude(status=Order.DELIVERED)
        num_pages, page = query.paginate(page_no)
        return dict(orders=page.detail(), num_pages=num_pages)


class OrderCallBackView(View):
    def post(self, request):
        return redirect(PAYMENT_CALLBACK_URL)


class OrderCancelView(View):
    def post(self, request):
        return redirect(PAYMENT_CANCEL_URL)
