from django.conf.urls import url
from .views import NewImage

urlpatterns = [
    url(r'^image/$', NewImage.as_view(), name='upload-image'),
]
