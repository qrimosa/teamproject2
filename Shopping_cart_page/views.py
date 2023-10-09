from django.shortcuts import render

# Create your views here.
def Shopping_cart_page(request):
    return render(request, 'Shopping_cart_page/shopping_cart_page.html')