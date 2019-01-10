from django.conf.urls import url
from .views import (get_all_post)

urlpatterns = [
    url(r'^$', get_all_post, name='list')
]
