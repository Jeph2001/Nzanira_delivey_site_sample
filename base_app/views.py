from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from .models import SignUp
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
            return HttpResponseRedirect('Hello world')
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
                    return HttpResponseRedirect('Location/')
                else:
                    return login_form.add_error(None, 'INCORRECT PASSWORD')
            except SignUp.DoesNotExist:
                return login_form.add_error(None, "We don't know you")
    
    else:
            login_form = LoginForm()
    return render(request, 'login_page.html', {'login_form': login_form})


            

