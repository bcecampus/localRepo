"""RegandLoginPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve

from RegAndLoginApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^reg/',views.Reg_View),
    url(r'^login/upload_img/',views.upload_img),
    url(r'^login/$',views.login),
    url(r'^login/(?P<date_recieved>[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{6})/(?P<name_recieved>[a-zA-Z]+)/$', views.like),

    # url(r'^login/',views.mode),
    url(r'^$',views.Login_View),
    url(r'^library/',views.library),
    url(r'^logout/',views.logout),
    url(r'^action/',views.action),
    url(r'^like/',views.like),
    url(r'^comment/(?P<date_recieved>[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{6})/(?P<name_recieved>[a-zA-Z]+)/$',views.comment),
    url(r'^branch_info/',views.branch_info),
    url(r'^reset_password/',views.reset_password),
    url(r'^reset/',views.sendmail),
    url(r'^newPassword/(?P<otp_recieved>[0-9]+)/(?P<user_name>[a-zA-Z]+)/',views.newPassword),
    #url(r'^comment/(?P<date_recieved>[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{6})/(?P<name_recieved>[a-zA-Z]+)/upload_img/',views.upload_img)
    url(r'^online/',views.active_member)

]

if settings.DEBUG:
    urlpatterns+=[
        url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,}),
    ]