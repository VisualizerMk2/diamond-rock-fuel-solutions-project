from django.http import HttpResponse
from django.shortcuts import render
from users.forms import CustomUserCreationForm
from users.models import CustomUser
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.


def home(request):
    form = CustomUserCreationForm(request.POST or None)
    context = {
      "form": form
    }
    if form.is_valid():
      form.save()
      form = CustomUserCreationForm()
    return render(request, 'pages/home.html', context)


