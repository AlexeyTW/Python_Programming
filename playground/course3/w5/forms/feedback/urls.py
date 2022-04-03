
from django.conf.urls import url
from .views import FeedbackCreateView, SchemaView, MarshView
from . import views

urlpatterns = [
    url('add/', views.FeedbackCreateView.as_view(), name='feedback-create')
]
