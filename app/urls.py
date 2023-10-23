from django.urls import path

from .views import (
create_signnow_document,
)

urlpatterns = [
    # path("server/", webhook),
    path("create_signnow_document/", create_signnow_document),

    ]
