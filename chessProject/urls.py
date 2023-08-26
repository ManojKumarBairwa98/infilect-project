from django.urls import path
from django.urls.conf import include
from chessProject import views as Views
from rest_framework import routers


urlpatterns = [
    path("chees",Views.get_user_profile, name="chees"),


]