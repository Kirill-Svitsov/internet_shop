from django.urls import path

from items import views

app_name = 'items'

urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('item/<slug:item_slug>/', views.item, name='item'),
]
