from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('product_details/<int:pk>',views.product_details,name='product_details'),
    path('category/<str:foo>', views.category, name= 'category'),
    path('register/',views.signup_user,name='signup'),
    path('login/',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
]
