from django.shortcuts import render

# Create your views here.
def startPage(request):
    return render(request, "online_shop/start_page.html")

def basket(request):
    return render(request, "online_shop/basket.html")