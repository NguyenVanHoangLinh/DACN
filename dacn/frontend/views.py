from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Categories, Website, Discount
from django.urls import resolve, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
        all_categories = Categories.objects.all()
        all_websites = Website.objects.all()
        all_discounts = Discount.objects.order_by('-id')
        return render(request, 'index.html',{'categories': all_categories,'websites': all_websites,'discounts': all_discounts})
def single(request, id):
    """detail request"""
    discount = Discount.objects.get(id=id)
    all_categories = Categories.objects.all()
    all_websites = Website.objects.all()
    current_url = request.get_full_path()
    return render(request, 'single.html', {'discount': discount,'categories': all_categories,'websites': all_websites,'current_url': current_url})
def category(request, name):
    """category request"""
    all_categories = Categories.objects.all()
    all_websites = Website.objects.all()
    discount = Discount.objects.filter(category_name=name)
    category = Categories.objects.get(name=name)
    return render(request, 'category.html', {'discount': discount,'categories': all_categories,'websites': all_websites,'category':category})
def signup(request):
        if request.method == 'POST':
                form = UserCreationForm(request.POST)
                all_categories = Categories.objects.all()
                all_websites = Website.objects.all()
                all_discounts = Discount.objects.order_by('-id')
                if form.is_valid():
                        form.save()
                        username = form.cleaned_data.get('username')
                        raw_password = form.cleaned_data.get('password1')
                        user = authenticate(username=username, password=raw_password)
                        login(request, user)
                        return redirect('/',categories=all_categories,websites=all_websites,discounts=all_discounts) 
        else:
                form = UserCreationForm()
                all_categories = Categories.objects.all()
                all_websites = Website.objects.all()
        return render(request, 'signup.html', {'form': form,'categories': all_categories,'websites': all_websites}) 
def logout(request):
        django_logout(request)
        all_categories = Categories.objects.all()
        all_websites = Website.objects.all()
        all_discounts = Discount.objects.order_by('-id')
        return redirect('/',categories=all_categories,websites=all_websites,discounts=all_discounts) 
def login_view(request):
        if request.method == 'POST':
                all_categories = Categories.objects.all()
                all_websites = Website.objects.all()
                all_discounts = Discount.objects.order_by('-id')
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user)
                        return redirect('/',categories=all_categories,websites=all_websites,discounts=all_discounts)
                else:
                        context = 'thong tin nhap sai'
                        all_categories = Categories.objects.all()
                        all_websites = Website.objects.all()
                        all_discounts = Discount.objects.order_by('-id')
                        return redirect('/',categories=all_categories,websites=all_websites,discounts=all_discounts,context=context)