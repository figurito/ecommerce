from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import UserRegisterForm
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from .models import Product


# Create your views here.
def registrar(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            messages.success(request, "Usuario %s Creado Correctamente" %username)
            return redirect('iniciarSesion')
    else:
        form=UserRegisterForm(request.POST)
    context={'formulario':form}
    return render(request, 'store/registrar.html', context )

def iniciarSesion(request):
    if request.method== 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store')
    context={}
    return render(request, 'store/iniciarSesion.html', context )

def logoutUser(request):
    logout(request)
    return redirect('iniciarSesion')
    

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)

def get(request):
    busqueda = request.GET.get('busqueda')
    result = Product.objects.filter(name=busqueda)
    return render(request, 'store/store_buscar.html', {"data":result})
  
def resultado(request):
    busqueda = request.GET.get('busqueda')
    result = Product.objects.filter(name=busqueda)
    mensaje=""
    for i in result:
        mensaje="Nombre: %s, Precio: %s" %(mensaje, i.name, i.price)
    return HttpResponse(mensaje)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)