"""
URL configuration for Out_of_Ghar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, re_path,path
from .views import homepage, blog_approval, Packages, blog_reports, unique_report, catch_all_view,hotel,travel,airline,lifestyle,change_password
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),

    # Home page
    re_path(r'^$', homepage, name='home'),
    re_path(r'^approve/$', blog_approval, name='approve_page'),
    re_path(r'^Packages/$', Packages, name='Packages'),
    re_path(r'^reports_list/$', blog_reports, name='reports_list'),
    re_path(r'^reports_list/(?P<report_id>\d+)/$', unique_report, name='unique_report'),
    path('hotels/', hotel, name='hotel'),
    path('airlines/', airline, name='airline'),
    path('travels/', travel, name='travel'),
    path('lifestyle/', lifestyle, name='lifestyle'),
    path('change_password', change_password, name='change_password'),

    # accounts
    re_path(r'^account/', include('accounts.urls')),

    # blog
    re_path(r'^blog/', include('blog.urls')),

    # userProfile
    re_path(r'^userProfile/', include('userProfile.urls')),

    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^accounts/', include('allauth.socialaccount.urls')),

    re_path(r'^.*/$', catch_all_view, name='catch_all_view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
