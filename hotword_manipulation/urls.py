from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^home/$', views.index),
    url(r'^pullblack/(?P<queryword>[a-zA-Z0-9\u4e00-\u9fa5]+)$', views.pullblack,name='pullblack')
]
