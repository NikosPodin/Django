from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Geekshop - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)

    else:
        form = UserRegisterForm()
    context = {
        'title': 'Geekshop - Регистрация',
        'form': form
    }
    return render(request, 'users/register.html', context)

# @login_requires
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST,
                               files=request.FILES,
                               instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваш профиль был успешно обновлен")
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            messages.error(request, "Профиль не сохранён")
    context = {
        'title': 'Geekshop - Профайл',
        'form': UserProfileForm(instance=request.user),
            # 'baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))