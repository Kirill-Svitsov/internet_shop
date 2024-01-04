from django.urls import path

from items import views

app_name = 'items'
 
urlpatterns = [
    path('', views.catalog, name='index'),
    path('item/', views.item, name='item'),
]