
from django.conf.urls import url
from .views import FormDummyView

urlpatterns = [
    url('', FormDummyView.as_view())
]
