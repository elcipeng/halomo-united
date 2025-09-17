from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # daftar produk
    path('add/', views.add_form, name='add_form'),
    path('detail/<int:id>/', views.detail, name='detail'),

    # data delivery
    path('xml/', views.data_xml, name='data_xml'),
    path('json/', views.data_json, name='data_json'),
    path('xml/<int:id>/', views.data_xml_by_id, name='data_xml_by_id'),
    path('json/<int:id>/', views.data_json_by_id, name='data_json_by_id'),

    # halaman utama
    path('main/', views.show_main, name='show_main'),
]
