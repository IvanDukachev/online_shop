from django.shortcuts import render
from .models import Product

# Create your views here.
def startPage(request):
    return render(request, "online_shop/start_page.html")

def basket(request):
    archive = Product.objects.all()
    return render(request, "online_shop/basket.html", {"archive": archive})

def loginUser(request):
    return render(request, "online_shop/login_user.html")

def registerUser(request):
    return render(request, "online_shop/register_user.html")

def personalAccount(request):
    return render(request, "online_shop/personal_account.html")
