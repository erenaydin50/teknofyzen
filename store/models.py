from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)  # Kategori adı
    image = models.ImageField(upload_to='category_images/')  # Kategori görseli

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    name = models.CharField(max_length=200)  # Ürün adı
    description = models.TextField()  # Ürün açıklaması
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Ürün fiyatı
    image = models.ImageField(upload_to='products/')  # Ürün görseli
    created_at = models.DateTimeField(auto_now_add=True)  # Ürün oluşturulma tarihi
    is_best_seller = models.BooleanField(default=False)  # ✅ En çok satan etiketi

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"