# main/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
import json

from .models import Product
from .forms import ProductForm


@login_required(login_url='/login/')
def show_main(request):
    """Menampilkan halaman utama dengan daftar produk."""
    product_list = Product.objects.filter(user=request.user)
    
    context = {
        'npm': '2406406742',
        'name': request.user.username,
        'class': 'PBP D',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)

@login_required(login_url='/login/')
def create_product(request):
    """Menampilkan form dan memproses pembuatan produk (metode form tradisional)."""
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect("main:show_main")
    else:
        form = ProductForm()
    return render(request, "create_product.html", {"form": form})

@login_required(login_url='/login/')
def show_product(request, id):
    """Menampilkan detail satu produk."""
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, "product_detail.html", context)

@login_required(login_url='/login/')
def edit_product(request, id):
    """Menampilkan form dan memproses edit produk (metode form tradisional)."""
    product = get_object_or_404(Product, pk=id, user=request.user)
    form = ProductForm(request.POST or None, instance=product)
    
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "edit_product.html", context)

@login_required(login_url='/login/')
def delete_product(request, id):
    """Menghapus produk (metode form tradisional)."""
    product = get_object_or_404(Product, pk=id, user=request.user)
    product.delete()
    return redirect(reverse('main:show_main'))


@ensure_csrf_cookie
def login_view(request):
    """Menangani GET (menampilkan halaman) dan POST (login via AJAX)."""
    if request.method == "GET":
        return render(request, "login.html")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"status": True, "message": "Login successful!"}, status=200)
        else:
            return JsonResponse({"status": False, "message": "Invalid username or password."}, status=401)
    
    return JsonResponse({"status": False, "message": "Invalid request method."}, status=405)


def logout_user(request):
    """Menangani logout dan redirect ke halaman login dengan notifikasi."""
    logout(request)
    response = redirect(reverse('main:login') + '?logout=true')
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def register_ajax(request):
    """Menangani GET (menampilkan halaman) dan POST (register via AJAX)."""
    if request.method == "GET":
        return render(request, "register.html")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Validasi input
        if not username or not password:
            return JsonResponse({
                "status": False, 
                "message": "Username and password are required."
            }, status=400)

        # Cek username sudah ada
        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "status": False, 
                "message": "Username is already taken."
            }, status=409)

        # Buat user baru
        try:
            User.objects.create_user(username=username, password=password)

            return JsonResponse({
                "status": True, 
                "message": "Registration successful!"
            }, status=201)
        except Exception as e:
            return JsonResponse({
                "status": False, 
                "message": f"Registration failed: {str(e)}"
            }, status=500)

    return JsonResponse({
        "status": False, 
        "message": "Invalid request method."
    }, status=405)

def show_json(request):
    """Mengembalikan semua produk dalam format JSON."""
    product_list = Product.objects.all()
    data = [{
        'id': p.id, 'name': p.name, 'price': float(p.price), 'description': p.description,
        'thumbnail': p.thumbnail or None, 'category': p.category, 'is_featured': p.is_featured,
        'user_id': p.user.id if p.user else None,
    } for p in product_list]
    return JsonResponse(data, safe=False)

def show_xml(request):
    """Mengembalikan semua produk dalam format XML."""
    product_list = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", product_list), content_type="application/xml")

def show_json_by_id(request, id):
    """Mengembalikan satu produk dalam format JSON berdasarkan ID."""
    product = get_object_or_404(Product, pk=id)
    return HttpResponse(serializers.serialize("json", [product]), content_type="application/json")

def show_xml_by_id(request, id):
    """Mengembalikan satu produk dalam format XML berdasarkan ID."""
    product = get_object_or_404(Product, pk=id)
    return HttpResponse(serializers.serialize("xml", [product]), content_type="application/xml")


@csrf_exempt
@login_required(login_url='/login/')
@require_http_methods(["POST"])
def create_product_ajax(request):
    """Membuat produk baru via AJAX POST request."""
    data = request.POST
    try:
        price = int(data.get("price"))
        if price < 0:
            return JsonResponse({"error": "Price must be a positive number"}, status=400)
    except (ValueError, TypeError):
        return JsonResponse({"error": "Price must be a valid number"}, status=400)
    
    product = Product.objects.create(
        name=data.get("name"), price=price, description=data.get("description"),
        category=data.get("category"), thumbnail=data.get("thumbnail"),
        is_featured=data.get("is_featured") == "on", user=request.user,
    )
    return JsonResponse({"message": "Product created successfully", "id": product.id}, status=201)

@csrf_exempt
@login_required(login_url='/login/')
@require_http_methods(["PUT"])
def update_product_ajax(request, id):
    """Mengupdate produk via AJAX PUT request."""
    try:
        product = get_object_or_404(Product, pk=id, user=request.user)
        data = json.loads(request.body)
        
        product.name = data.get('name', product.name)
        product.price = int(data.get('price', product.price))
        product.description = data.get('description', product.description)
        product.save()
        
        return JsonResponse({"message": "Product updated successfully"})
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found or permission denied"}, status=404)
    except (ValueError, TypeError):
        return JsonResponse({"error": "Price must be a valid number"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
@login_required(login_url='/login/')
@require_http_methods(["DELETE"])
def delete_product_ajax(request, id):
    """Menghapus produk via AJAX DELETE request."""
    try:
        product = get_object_or_404(Product, pk=id, user=request.user)
        product.delete()
        return JsonResponse({"message": f"Product '{product.name}' deleted successfully"})
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found or permission denied"}, status=404)