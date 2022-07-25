from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('chatting/public_chatting/', views.redirect_into_lobby, name="redirect_into_lobby"),
    path("notify/",views.notify_group,name="notify")
]
