from django.urls import path
# from . import views
from .views import *

urlpatterns = [
    # path('', views.token_list)
    path('fcmtokens', FCMView.as_view()),
    path('newsposts', NewsView.as_view())
]
