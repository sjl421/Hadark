"""hadark URL Configuration

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
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from fs import views as fs_views

router = routers.DefaultRouter()
router.register(r'file', fs_views.FileViewSet, base_name='file')
router.register(r'user', fs_views.UserViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('mainapp.urls', namespace="api")),
    url(r'^fs/', include(router.urls)),
    url(r'^authentication/', include('authentication.urls', namespace="authentication")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^file-api/$', fs_views.get_file_content),
]
