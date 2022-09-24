from django.contrib import admin
from django.urls import path, include
from main import views

from django.conf.urls.static import static
from django.urls import path, include
from main import views, settings


urlpatterns = [
    path('', views.index_home, name='index_home'),
    path('about_shop/', views.about_shop, name='about_shop'),
    path('admin/', admin.site.urls),
    path('auth_log_reg/', include('authentication.urls')),
    path('shop/', include('shop.urls')),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

