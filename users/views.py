from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from users.forms import UserChangeForm
from .models import CustomUser


from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name='pages/signup.html'

def profile(request):
    context = {
        "user": request.user
    }
    return render(request, 'pages/profile.html', context)

def edit_profile(request):

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            print('Form successfully saved')
            return redirect('/users/profile')
    
    else:
        form = CustomUserChangeForm(instance=request.user)
        context = {
            "form": form,

        }
        return render(request, 'pages/edit_profile.html', context)


    return render(request, 'pages/edit_profile.html', context)

def quotes(request):
    return render(request, 'pages/quotes.html')

