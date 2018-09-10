from django.conf.urls import include, url
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.post_list),
]