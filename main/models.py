from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('sepatu', 'Sepatu'),
        ('aksesoris', 'Aksesoris'),
        ('peralatan', 'Peralatan Olahraga'),
        ('lainnya', 'Lainnya'),
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, blank=True)
    is_featured = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

