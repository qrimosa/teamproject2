from django.shortcuts import render

# Create your views here.
def product_page(request):
    return render(request, 'Product_page/Product_page.html')
