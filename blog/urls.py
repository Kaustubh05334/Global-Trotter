from django.urls import re_path,path
from .views import (
    blogPostPage, preview_blog, blog_details, delete_blog, search,
    like_blog, report_blog, delete_comment
)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    re_path(r'^postblog/$', blogPostPage, name='blog_post_page'),
    path('preview/<slug:title>/<int:blog_id>/', preview_blog, name='preview_blog'),
    path('like/<slug:title>/<int:blog_id>/', like_blog, name='like_blog'),
    path('view/<slug:title>/<int:blog_id>/', blog_details, name='blog_details'),
    re_path(r'^blog/(?P<blog_id>\d+)/delete/$', delete_blog, name='delete_blog'),
    re_path(r'^search/$', search, name='search'),
    re_path(r'^delete_comment/(?P<blog_id>\d+)/(?P<comment_id>\d+)/$', delete_comment, name='delete_comment'),
    re_path(r'^report/(?P<blog_id>\d+)/$', report_blog, name='report_blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
