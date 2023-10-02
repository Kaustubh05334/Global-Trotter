from django.urls import re_path
from .views import profile_page, profile_view, reject_blog_page, all_notification
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^profile/$', profile_page, name='profile_page'),
    re_path(r'^profile/view/$', profile_view, name='profile_view'),
    re_path(r'^reject/(?P<ad_id>\d+)/$', reject_blog_page, name='rejected_notf'),
    re_path(r'^all_notf/$', all_notification, name='all_notf'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
