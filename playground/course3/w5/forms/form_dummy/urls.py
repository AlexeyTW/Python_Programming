
from django.conf.urls import url
from .views import FormDummyView, SchemaView

urlpatterns = [
    url('', SchemaView.as_view())
]
