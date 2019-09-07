from django.conf.urls import url
from apis.views import *

urlpatterns = [
    #url(r'^users/$' UserList.as_view(), name = 'users'),
    url('users/$', UserList.as_view(), name = 'user')
]