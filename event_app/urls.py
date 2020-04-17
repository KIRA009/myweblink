from django.urls import path

from .views import *
from utils import login_required, pro_required

unauth_urls = list(
    map(
        lambda x: path(x[0], x[1].as_view()),
        [
            ("register/", RegisterView),
            ("update/", UpdateView),
            ("colleges/", CollegeView),
            ("login/", LoginView),
            ("validate-email/", SendValidateEmailView),
            ("validate/<int:user_id>/<uuid:secret>/", CompleteValidateEmailView),
            ("user/", GetUserView),
        ],
    )
)

auth_urls = list(
    map(
        lambda x: path(x[0], login_required(x[1].as_view())),
        [
            ("upload/profile/", UploadProfilePicView),
            ("links/", UserLinkView),
            ("update-link-sequence/", UpdateLinkSequenceView),
            ("upload-icon/", UploadIconView),
        ],
    )
)

pro_urls = list(
    map(
        lambda x: path(x[0], pro_required(login_required(x[1].as_view()))),
        [
            ("feature/header/", ProModeHeaderView),
            ("feature/background/", ProModeBgView),
            ("feature/", ProModeView),
        ],
    )
)

urlpatterns = unauth_urls + auth_urls + pro_urls
