"""KampusApk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from app.config import setting

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^mahasiswa/', include('management.mahasiswa.urls', namespace="mahasiswa")),
]

urlpatterns +=  staticfiles_urlpatterns()
urlpatterns += static(setting.MEDIA_URL, document_root=setting.MEDIA_ROOT)