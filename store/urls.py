from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from store import views

urlpatterns = [
    path('', views.product_list, name='home'),  # Anasayfa
    path('urunler/', views.product_list, name='product_list'),
    path('satistakiler/', views.for_sale, name='for_sale'),  # Satıştaki tüm ürünler + kategoriler
    path('satistakiler/<int:category_id>/', views.for_sale, name='for_sale_by_category'),  # ✅ Kategoriye göre filtreleme
    path('iletisim/', views.contact_view, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('siparisler/', views.orders, name='orders'),
    path('satın-al/<int:pk>/', views.satın_al, name='satın_al'),
    path('odeme/<int:pk>/', views.odeme, name='odeme'),
    path('odeme-basarili/', views.payment_success, name='payment_success'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('', views.product_list, name='home'),
]

# Medya dosyaları
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)