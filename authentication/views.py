from django.shortcuts import render, redirect
from .forms import LogInForm, RegisterForm
from django.contrib.auth import logout, authenticate, login
from django.views.generic import TemplateView



# Create your views here.
def log_in(request):
    context = {'login_form': LogInForm()}
    if request.method == 'POST':
        login_form = LogInForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                context = {'login_form': login_form,
                           'attention': f"The user with username {username} and password was not found!"
                }
        else:
            context= {'login_form': LogInForm()}


    return render(request, 'authentication/log_in.html', context)


class RegisterView(TemplateView):
    template_name = 'authentication/register.html'

    def get(self, request):
        user_form = RegisterForm()
        context = {'user_form': user_form}
        return render(request, 'authentication/register.html', context)
    def post(self, request):
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('index')
        context = {'user_form': user_form}
        return render(request, 'authentication/register.html', context)


def log_out(request):
    logout(request)
    return redirect('index')
