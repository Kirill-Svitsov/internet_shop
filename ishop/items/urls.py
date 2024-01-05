from django.urls import path

from items import views

app_name = 'items'
 
urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('item/<slug:item_slug>/', views.item, name='item'),
]