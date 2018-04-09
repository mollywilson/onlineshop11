from django.conf.urls import url
from . import views

urlpatterns = [
    # /frontpage/
    url(r'^$', views.index, name='index'),

    # /frontpage/ album_id
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
]
