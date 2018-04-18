from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'^id/(?P<user_id>\d+)/$', views.userprofile),
    url(r'^str', views.userprofile1),
    url(r'^', views.userprofile),
]