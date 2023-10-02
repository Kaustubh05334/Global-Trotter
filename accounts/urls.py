from django.urls import re_path, include
from .views import login_page, register_user, logout_page

urlpatterns = [
    re_path(r'^login/$', login_page, name='login_page'),
    re_path(r'^register/$', register_user, name='register_user'),
    re_path(r'^logout/$', logout_page, name='logout_page'),
]
