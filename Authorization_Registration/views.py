from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError

# Create your views here.
def Authorization_Registration(request):
    return render(request,'Authorization_Registration/Authorization_Registration.html')

def Registration(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        login = request.POST.get('login')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        checkbox = request.POST.get('checkbox')
        context['email'] = email
        context['login'] = login
        context['password']  = password
        context['confirm_password'] = confirm_password 
           
        if login and password and email and confirm_password and checkbox:
            if len(password) >= 8:
                if password == confirm_password:
                    try:
                        User.objects.create_user(username = login, email = email, password = password)
                        return redirect('Authorization')
                    except IntegrityError:
                        context['error'] = 'Такий користувач вже існує!'
                else:
                    context['error'] = 'Паролі не співпадають!'
            else:
                context['error'] = 'Пароль повинен бути більше ніж 7 символів!'
        else:
            context['error'] = 'Ви не заповнили усі поля(галочку)!'
    return render(request, 'Authorization_Registration/registration.html', context)

def Authorization(request):
    context = {}
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        context['error'] = 'Ти вже авторизувався'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        context['username'] = username
        if username and password:
            user = authenticate(username = username, password = password)
            print(user)
            if user:
                login(request, user)
            else:
                context['error'] = 'Логін aбо пароль невірний'
        else:
            context['error'] = 'Заповніть всі поля'
    return render(request, 'Authorization_Registration/authorization.html', context)


    
    