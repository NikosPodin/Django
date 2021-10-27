# from django.contrib.auth.mixins import LoginRequiredMixin

from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
# from django.utils.decorators import method_decorator
from django.views.generic import FormView, UpdateView #ListView,

from geekshop.mixin import BaseClassContextMixin, UserDispatchMixin #CustomDispatchMixin,
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm, UserProfileEditForm
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
# from baskets.models import Basket
# from django.contrib.auth.decorators import login_required, user_passes_test
from users.models import User


class LoginListView(LoginView, BaseClassContextMixin):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Geekshop -Авторизация'


# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#
#     context = {
#         'title': 'Geekshop - Авторизация',
#         'form': form
#     }
#     return render(request, 'users/login.html', context)

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегистрировались!')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegisterForm()
#     context = {
#         'title': 'Geekshop - Регистрация',
#         'form': form
#     }
#     return render(request, 'users/register.html', context)

class RegisterListView(FormView, BaseClassContextMixin):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    title = 'Geekshop - Регистрация'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            if send_verify_link(user):
                messages.success(request, f'Вы успешно зарегистрировались.\n На ваш email '
                                          f'{user.email} отправлено письмо со '
                                          f'ссылкой для активации аккаунта {user.username}')
            return redirect(self.success_url)
        else:
            messages.warning(request, f'{form.errors}')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST,
#                                files=request.FILES,
#                                instance=request.user)  # instance - обновит данные, а не создаст новую запись
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Ваш профиль был успешно обновлен")
#             return HttpResponseRedirect(reverse('users:profile'))
#         else:
#             messages.error(request, "Профиль не сохранён")
#
#     context = {
#         'title': 'Geekshop - Профайл',
#         'form': UserProfileForm(instance=request.user),  # instance - заполнит поля текущими значениями
#         'baskets': Basket.objects.filter(user=request.user),
#     }
#     return render(request, 'users/profile.html', context)

class ProfileFormView(UpdateView, BaseClassContextMixin, UserDispatchMixin):  # CustomDispatchMixin, LoginRequiredMixin
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    title = 'Geekshop - Профайл'

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

    # @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    # def dispatch(self, request, *args, **kwargs):
    #     return super(ProfileFormView, self).dispatch(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super(ProfileFormView, self).get_context_data(**kwargs)
    #     context['baskets'] = Basket.objects.filter(user=self.request.user)
    #     return context
    # Так как через contex_processor уже передаётся

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES, instance=self.get_object())
        form_edit = UserProfileEditForm(data=request.POST, instance=request.user.userprofile)
        if form.is_valid() and form_edit.is_valid():
            form.save()
            return redirect(self.success_url)
        return redirect(self.success_url)


def send_verify_link(user):
    verify_link = reverse('users:verify', args=[user.email, user.activation_key])
    subject = f"Для активации учетной записи {user.username} пройдите по ссылке"
    message = f"Для подтвердения учетной записи {user.username} на портале \n {settings.DOMAIN_NAME}{verify_link}"
    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user and user.activation_key == activation_key and not user.is_activation_key_expired():
            user.activation_key = ''
            user.activation_key_created = None
            user.is_active = True
            user.save()
            auth.login(request, user)
        return render(request, 'users/verification.html')
    except Exception as e:
        return HttpResponseRedirect(reverse('index'))


class Logout(LogoutView):
    template_name = 'mainapp/index.html'

# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))
