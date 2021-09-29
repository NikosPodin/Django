from django.shortcuts import render

# Create your views here.
def login(request):
    contex ={
        'title': 'Geekshop - Авторизация'
     }
    return render(request,'users/login.html', contex)

def register(request):
    contex: {
        'title': 'Geekshop - Регистрация'
    }
    return render(request,'users/register.html', contex)