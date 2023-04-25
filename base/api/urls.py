from django.urls import path
from . import views
from .views import ExampleView

urlpatterns = [
    # path('', views.token_list)
    path('', ExampleView.as_view())
]
