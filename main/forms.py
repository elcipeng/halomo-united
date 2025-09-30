from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'thumbnail', 'category', 'is_featured']
        widgets = {
                'name': forms.TextInput(attrs={
                    'class': 'w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent transition-colors',
                    'placeholder': 'Contoh: Bola Jabulani Piala Dunia 2010'
                }),
                'price': forms.NumberInput(attrs={
                    'class': 'w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent transition-colors',
                    'placeholder': 'Contoh: 150000'
                }),
                'category': forms.Select(attrs={
                    'class': 'w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent transition-colors'
                }),
                'description': forms.Textarea(attrs={
                    'class': 'w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent transition-colors',
                    'rows': 5,
                    'placeholder': 'Jelaskan detail produk Anda di sini...'
                }),
                'thumbnail': forms.URLInput(attrs={
                    'class': 'w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent transition-colors',
                    'placeholder': 'https://example.com/image.jpg'
                }),
                'is_featured': forms.CheckboxInput(attrs={
                    'class': 'h-5 w-5 text-green-600 border-gray-300 rounded focus:ring-green-500'
                }),
            }
        