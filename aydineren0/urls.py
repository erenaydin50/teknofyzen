from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('urunler/', include('store.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('store.urls')),  # Anasayfa yönlendirmesi burada zaten var
    path('accounts/', include('django.contrib.auth.urls')),
]

# Statik ve medya dosyaları
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)