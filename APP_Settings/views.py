from django.shortcuts import render

# Create your views here.
def appsettings(request):
    return render(request, 'appsettings/base.html')


