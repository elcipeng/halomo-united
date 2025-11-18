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
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.utils.html import strip_tags
import json
from django.http import JsonResponse
from .models import Product
from .forms import ProductForm
from django.core import serializers

import requests

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Product  # sesuaikan nama model

from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.utils.html import strip_tags
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import json

@login_required
def my_products_json(request):
    qs = Product.objects.filter(user=request.user).values(
        'id','name','price','description','thumbnail','category','is_featured','user_id'
    )
    return JsonResponse(list(qs), safe=False)


@require_POST
@csrf_exempt
@login_required
def create_product_flutter(request):
    """
    Endpoint for Flutter/mobile clients.
    Accepts JSON body (preferred) or form-data.
    If the request has an authenticated session, use request.user.
    Otherwise, accept 'username' + 'password' in the JSON body to authenticate.
    """
    if request.method != "POST":
        return JsonResponse({"status": False, "message": "Invalid request method."}, status=405)

    # parse JSON if possible, otherwise fall back to form-encoded POST
    try:
        data = json.loads(request.body.decode('utf-8')) if request.body else {}
    except (json.JSONDecodeError, UnicodeDecodeError):
        # fallback to POST data (FormData)
        data = request.POST.dict() if hasattr(request, 'POST') else {}

    # Determine user: prefer session user, otherwise try credentials in payload
    user = request.user if request.user.is_authenticated else None
    if not user:
        username = data.get("username")
        password = data.get("password")
        if username and password:
            user = authenticate(request, username=username, password=password)

    if not user:
        return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)

    name = strip_tags(data.get("name", "")).strip()
    description = strip_tags(data.get("description", "")).strip()
    category = (data.get("category", "") or "").strip()
    thumbnail = (data.get("thumbnail", "") or "").strip()
    is_featured = bool(data.get("is_featured", False))
    price_raw = data.get("price", None)

    errors = {}

    if not name:
        errors["name"] = "Name is required"
    elif len(name) < 3:
        errors["name"] = "Name too short"

    if not description:
        errors["description"] = "Description is required"
    elif len(description) < 10:
        errors["description"] = "Description too short"

    if price_raw is None or price_raw == "":
        errors["price"] = "Price is required"
    else:
        try:
            price = float(price_raw)
            if price <= 0:
                errors["price"] = "Price must be greater than 0"
        except (ValueError, TypeError):
            errors["price"] = "Price must be a number"

    if thumbnail:
        validator = URLValidator()
        try:
            validator(thumbnail)
        except ValidationError:
            errors["thumbnail"] = "Invalid thumbnail URL"

    if errors:
        return JsonResponse({"status": "error", "errors": errors}, status=400)

    new_product = Product.objects.create(
        name=name,
        description=description,
        price=price,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user,
    )

    return JsonResponse({"status": "success", "id": new_product.id}, status=201)


def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    


def sort_products(request):
    sort_o = request.GET.get('desc', 'asc')

    if sort_o == 'desc':
        products = product.object.all().ordey_by('-price')
    else:
        products = product.object.all().ordey_by('price')

    data = serializers.serialize('json', products)
    return HttpResponse(data, content_type='halomo_united/json')


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
    """
    Return products as JSON.
    Query params:
      - ?user_only=true  -> returns only authenticated user's products (requires session)
      - ?user_id=NN      -> returns products for user with id NN
    Default: return all products.
    """
    user_only = request.GET.get("user_only") == "true"
    user_id = request.GET.get("user_id")

    if user_only:
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Authentication required"}, status=401)
        product_list = Product.objects.filter(user=request.user)
    elif user_id:
        product_list = Product.objects.filter(user__id=user_id)
    else:
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