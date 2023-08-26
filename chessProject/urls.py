from django.urls import path
from django.urls.conf import include
from chessProject import views as Views
from rest_framework import routers


urlpatterns = [
    path(r"chees/<str:slugName>",Views.get_chees_moves, name="chees"),

# r'^blog/(?P<slug>[-\w]+)/$'
]