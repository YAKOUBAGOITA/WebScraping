from django.shortcuts import render, redirect
from .forms import MyUserCreationForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Customer, Product
from . import scrapper

def shop(request):
    q = request.GET.get('q', '')  # Get the search query from the URL
    sort_option = request.GET.get('sort_option', '')  # Get the sorting option from the URL

    products = scrapper.product_scraper(q)

    # Handle sorting based on the sort_option
    if sort_option == "Name (A - Z)":
        products = dict(sorted(products.items(), key=lambda item: item[0]))
    elif sort_option == "Name (Z - A)":
        products = dict(sorted(products.items(), key=lambda item: item[0], reverse=True))
    elif sort_option == "Price (Low - High)":
        products = dict(sorted(products.items(), key=lambda item: int(item[1]['price'][1:].replace(',', '')) if item[1]['price'] is not None else 0))
    elif sort_option == "Price (High - Low)":
        products = dict(sorted(products.items(), key=lambda item: int(item[1]['price'][1:].replace(',', '')) if item[1]['price'] is not None else 0, reverse=True))
    elif sort_option == "Rate (High - Low)":
        products = dict(sorted(products.items(), key=lambda item: float(item[1]['rate']) if item[1]['rate'] is not None else -float('inf'), reverse=True))
    elif sort_option == "Rate (Low - High)":
        products = dict(sorted(products.items(), key=lambda item: float(item[1]['rate']) if item[1]['rate'] is not None else 0.0))


    context = {
        'products': products,
        'q': q,  # Pass the search query back to the template
    }
    return render(request, 'base/shop.html', context)

def loginPage(request):
    page = 'login'
    login_form = UserForm()

    if request.user.is_authenticated:
        return redirect('shop')

    if request.method == 'POST':
        messages.success(request, None)
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = Customer.objects.get(username=username)
        except Customer.DoesNotExist:  # Catch the specific exception
            messages.error(request, 'User does not exist')
            return redirect('login')  # Redirect back to the login page

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop')
        else:
            messages.error(request, "Username and password do not match")

    context = {'page': page, 'login_form': login_form}
    return render(request, 'base/login-register.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('shop')
    
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('shop')
        else:
            messages.error(request, 'An error occured during registration')
    return render(request, "base/login-register.html", {'form':form})

def logoutUser(request):
    logout(request)
    return redirect('shop')

