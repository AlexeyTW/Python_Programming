
from django.conf.urls import url
from .views import FormDummyView, SchemaView, MarshView

urlpatterns = [
    url('', FormDummyView.as_view())
]
