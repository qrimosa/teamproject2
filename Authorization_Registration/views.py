from django.shortcuts import render

# Create your views here.
def Authorization_Registration(request):
    return render(request,'Authorization_Registration/Authorization_Registration.html')
def Registration(request):
    return render(request, 'Authorization_Registration/registration.html')
def Authorization(request):
    return render(request, 'Authorization_Registration/authorization.html')