from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm

def show_main(request):
    context = {
        'nama_aplikasi': 'HaloMo United',
        'name': 'Justin Dwitama Seniang',
        'class': 'PBP D',
    }
    return render(request, "main.html", context)

# 1. XML
def data_xml(request):
    data = serializers.serialize("xml", Product.objects.all())
    return HttpResponse(data, content_type="application/xml")

# 2. JSON
def data_json(request):
    data = serializers.serialize("json", Product.objects.all())
    return HttpResponse(data, content_type="application/json")

# 3. XML by ID
def data_xml_by_id(request, id):
    obj = get_object_or_404(Product, pk=id)
    data = serializers.serialize("xml", [obj])
    return HttpResponse(data, content_type="application/xml")

# 4. JSON by ID
def data_json_by_id(request, id):
    obj = get_object_or_404(Product, pk=id)
    data = serializers.serialize("json", [obj])
    return HttpResponse(data, content_type="application/json")

# Index / daftar produk
def index(request):
    data = Product.objects.all()
    return render(request, "index.html", {"data": data})

# Create product
def add_form(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

# Detail produk
def detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'product_detail.html', {'product': product})
