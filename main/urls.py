"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
<<<<<<< HEAD
from django.urls import path, include
from main import views
=======
from django.conf.urls.static import static
from django.urls import path, include
from main import views, settings
>>>>>>> 800faf1 (Initial commit)

urlpatterns = [
    path('', views.index_home, name='index_home'),
    path('about_shop/', views.about_shop, name='about_shop'),
    path('admin/', admin.site.urls),
    path('auth_log_reg/', include('authentication.urls')),
    path('shop/', include('shop.urls')),

]
<<<<<<< HEAD
=======

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 800faf1 (Initial commit)
