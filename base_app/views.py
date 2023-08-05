from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import SignUpForm, LoginForm, LocationForm, PaymentsForm
from .models import SignUp, Location, Products
# Create your views here.

def landing_page(request):
    return render(request, 'landing_page.html')


def base_page(request):
    return render(request, 'base_page.html')


def signup_page(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return HttpResponseRedirect('/login/')
    else:
        signup_form = SignUpForm()
    
    return render(request, 'signup_page.html', {'signup_form': signup_form})


def login_page(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            phone_number = login_form.cleaned_data['phone_number']
            password = login_form.cleaned_data['password']
            try:
                user = SignUp.objects.get(phone_number=phone_number)
                if user.password == password:
                    return HttpResponseRedirect('/location/')
                else:
                    return login_form.add_error(None, 'INCORRECT PASSWORD')
            except SignUp.DoesNotExist:
                return login_form.add_error(None, "We don't know you")
    
    else:
            login_form = LoginForm()
    return render(request, 'login_page.html', {'login_form': login_form})


def location_page(request):
    if request.method == 'POST':
        location_form = LocationForm(request.POST)
        if location_form.is_valid():
            location_form.save()
            return HttpResponseRedirect('/home/')
    else:
        location_form = LocationForm()
    
    return render(request, 'location_page.html', {'location_form': location_form})


def home_page(request):
    products = Products.objects.all()
    return render(request, 'home_page.html', {'products': products})

def get_products_details(request, products_id):
    deproduct = Products.objects.get(id=products_id)
    return render(request, 'details_page.html', {'deproduct': deproduct})


def payment_page(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.method == 'POST':
        payment_form = PaymentsForm(request.POST)
        if payment_form.is_valid():
            payment_form.fields['product_name'].initial = product.product_name
            payment_form.save()
            return HttpResponseRedirect('/thanking/')
    else:
        payment_form = PaymentsForm(initial={'product_name': product.product_name})
    
    return render(request, 'payments_page.html', {'payment_form': payment_form})


def thanking_page(request):
    return render(request, 'thanking_page.html')











            

