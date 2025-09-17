from django.urls import path
from main.views import show_main
from . import views

app_name = 'main'


urlpatterns = [
    path('xml/', views.data_xml, name='data_xml'),
    path('json/', views.data_json, name='data_json'),
    path('xml/<int:id>/', views.data_xml_by_id, name='data_xml_by_id'),
    path('json/<int:id>/', views.data_json_by_id, name='data_json_by_id'),

    #form
    path('', views.index, name='index'),
    path('add/', views.add_form, name='add_form'),
    path('detail/<int:id>/', views.detail, name='detail'),
]
