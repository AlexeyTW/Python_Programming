from django.conf.urls import url, include
from django.contrib import admin
from .views import index, topic_details

urlpatterns = [
    url(r'^index/', index),
    url(r'topic/(?P<pk>\d+)', topic_details, name='topic_details')
]