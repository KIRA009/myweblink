from django.views import View

from notifications.models import Notification
from notifications.validators import *


class GetNotificationsView(View):
	def get(self, request, date):
		page_no = int(request.GET.get('pageNo', 1))
		query = Notification.objects.filter(user=request.User)
		unread_notifs = query.filter(read_at=None).count()
		num_pages, notifications = query.filter(updated_at__date=date).order_by('-read_at').paginate(page_no)
		return dict(num_pages=num_pages, notifications=notifications.detail(), unread_notifs=unread_notifs)


class ReadNotificationView(View):
	@read_notification_schema
	def post(self, request):
		data = request.json
		Notification.objects.get(id=data['notif_id'], user=request.User).read()
		return dict(unread_notifs=Notification.objects.filter(user=request.User).filter(read_at=None).count())
