from django.urls import path, include

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('users-cart/', views.users_cart, name='users_cart'),
    path('users-orders/', views.users_orders, name='users_orders'),

]
