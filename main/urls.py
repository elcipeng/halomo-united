from django.urls import path
from . import views
from main.views import logout_user, edit_product, login_view

app_name = 'main'

urlpatterns = [
    # Main pages
    path('', views.show_main, name='show_main'),
    path('main/', views.show_main, name='show_main'),

    # Product detail
    path('product/<int:id>/', views.show_product, name='show_product'),

    # Data Delivery
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', views.show_json_by_id, name='show_json_by_id'),

    # Auth
    path('login/', login_view, name='login'),
    path('logout/', logout_user, name='logout'),
    path("register-ajax/", views.register_ajax, name="register_ajax"),

    # CRUD
    path('create-product/', views.create_product, name='create_product'),
    path('product/<int:id>/edit/', edit_product, name='edit_product'),
    path('product/<int:id>/delete/', views.delete_product, name='delete_product'),

    # AJAX CRUD
    path('create-product-ajax/', views.create_product_ajax, name='create_product_ajax'),
    path('update-product-ajax/<int:id>/', views.update_product_ajax, name='update_product_ajax'),
    path('delete-product-ajax/<int:id>/', views.delete_product_ajax, name='delete_product_ajax'),
]
