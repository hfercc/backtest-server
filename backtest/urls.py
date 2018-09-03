"""backtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from django.views.static import serve
from backtest.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from report.views import ReportsViewSet, upload_report
from rest_framework_jwt import views
from users.views import UserViewset, UserLogin, change_password
from file.views import download_key
import xadmin
router = DefaultRouter()
router.register(r'report', ReportsViewSet, base_name="reports")
router.register(r'users', UserViewset, base_name="users")

urlpatterns = [
    path(r'xadmin/', xadmin.site.urls),
    path(r'media/<path:path>', serve, {'document_root':MEDIA_ROOT}),
    re_path(r'^files/(?P<report_id>\d+)/$', download_key, name='download-file'),
    path(r'login/', UserLogin.as_view(), name='login'),
    path(r'upload/', upload_report, name='upload-report'),
    path(r'users/change_password/', change_password, name='change-password'),
    path('',include(router.urls)),
]
