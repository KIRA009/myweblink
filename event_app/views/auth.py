from django.views import View
import uuid

from event_manager.settings import PROFILECONTAINER
from utils import upload_file, delete_file
from event_app.models import Link


class UploadProfilePicView(View):
    def post(self, request):
        if request.User.profile_pic:
            delete_file(request.User.profile_pic)
        file = request.FILES.dict().get("photo")
        if file is None:
            request.User.profile_pic = None
        else:
            file_name = request.User.username + str(uuid.uuid4()) + file.name
            upload_file(file, file_name, PROFILECONTAINER)
            request.User.profile_pic = f"https://storageeventmanager.blob.core.windows.net/{PROFILECONTAINER}/{file_name}"
        request.User.save()
        return dict(message="Profile pic set successfully", data=request.User.detail())


class UserLinkView(View):
    def get(self, request):
        return dict(links=[link.detail() for link in request.User.links.all()])

    def post(self, request):
        data = request.json
        if "id" in data:
            link_id = data["id"]
            del data["id"]
            link = Link.objects.get(id=link_id)
            if link.user != request.User:
                return dict(error="User not authorized", status_code=401)
            Link.objects.filter(id=link_id).update(**data)
        else:
            link = Link.objects.create(**data, user=request.User)
        return dict(link=link.detail())

    def delete(self, request):
        data = request.json
        Link.objects.get(id=data["id"]).delete()
        return dict(message="The links are deleted")
