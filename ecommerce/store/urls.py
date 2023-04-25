from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('registrar/', views.registrar, name="registrar"),
	path('iniciarSesion/', views.iniciarSesion, name="iniciarSesion"),
	path('cerrarSesion/', views.logoutUser, name="cerrarSesion"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('buscar/', views.resultado, name="buscar"),
 

]