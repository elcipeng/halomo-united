from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=200)                     # nama item
    price = models.IntegerField(validators=[MinValueValidator(0)])  # harga; gunakan positive validator
    description = models.TextField(blank=True)                  # deskripsi panjang
    thumbnail = models.URLField(blank=True)                     # URL gambar (atau pakai ImageField jika upload)
    category = models.CharField(max_length=100, blank=True)     # kategori item
    is_featured = models.BooleanField(default=False)            # status unggulan

    def __str__(self):
        return self.name
