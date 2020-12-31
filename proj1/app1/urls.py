from django.urls import path
from . import views

urlpatterns=[
	path('',views.home,name='home'),
	path('products',views.products,name="products"),
	path('about',views.about,name="about"),
	path('register',views.register,name="register"),
	path('login',views.login,name="login"),
	path('contact',views.contact,name="contact"),
    path("logout",views.logout,name="logout")
]
