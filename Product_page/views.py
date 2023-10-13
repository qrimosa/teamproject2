from django.shortcuts import render

# Create your views here.
def product_page(request):
    return render(request, 'Product_page/Product_page.html')
def apple(request):
    return render(request, 'Product_page/apple.html')
def xiaomi(request):
    return render(request, 'Product_page/xiaomi.html')
def samsung(request):
    return render(request, 'Product_page/samsung.html')
def pixel(request):
    return render(request, 'Product_page/pixel.html')