from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect


class UserProfile(TemplateView):
    template_name = 'accounts/profile.html'
    
    
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:profile")
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return response
    

class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')


class MyLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True



