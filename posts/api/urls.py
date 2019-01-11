from django.conf.urls import url
from .views import (get_all_post, create_post)
from django.urls import path


urlpatterns = [
    url(r'^$', get_all_post, name='list'),
    path('create/', create_post)
]
