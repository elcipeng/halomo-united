from django.urls import path 
from . import views
from main.views import register, login_user, logout_user


app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('detail/<int:id>/', views.show_product, name='show_product'),

    # data delivery
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<int:product_id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:product_id>/', views.show_json_by_id, name='show_json_by_id'),

    # halaman utama
    path('main/', views.show_main, name='show_main'),

    # auth
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    # create product
    path('register/', register, name='register'),
    path("create-product/", views.create_product, name="create_product"),
]

