from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import LoginForm, LocationForm, PaymentsForm, UserForm, SignUpForm
from .models import  Location, Products, Payments, SignUp
from rest_framework import viewsets, permissions
from .serializers import PaymentsSerializer, ProductsSerializer, LocationSerializer, UserSerializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly

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
            # username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = SignUp.objects.get(phone_number=phone_number)
                # user = User.objects.get(username=username)
                if user.password == password:
                    return HttpResponseRedirect('/location/')
                else:
                    # return login_form.add_error(None, 'INCORRECT PASSWORD')
                    return login_form.add_error(None, 'INCORRECT PASSWORD')
            except User.DoesNotExist:
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
# @api_view(['GET', 'POST'])
# def payment_page(request):
#     if request.method == 'GET':
#         payment = Payments.objects.all()
#         serializer = PaymentsSerializer(payment, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = PaymentsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    


def thanking_page(request):
    return render(request, 'thanking_page.html')


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
















            

