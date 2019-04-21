from django.shortcuts import render
from .models import FuelQuote
from .forms import FuelQuoteModelForm
# Create your views here.

def quote_detail_page(request, id):
  obj = get_object_or_404(FuelQuote, id=id)
  context = {"object": obj}
  return render(request, 'pages/quote.html', context)


def quotes(request):
  if request.user.is_authenticated:
    my_qs = FuelQuote.objects.filter(user=request.user)
  context = {'object_list': my_qs}
  return render(request, 'pages/quote_list.html', context)

def get_quote(request):
  form = FuelQuoteModelForm(request.POST or None)
  if form.is_valid():
    obj = form.save(commit=False) 
    obj.user = request.user
    obj.save()
    form = FuelQuoteModelForm()
  context = {
    "form": form,
  }
  return render(request, 'pages/get_quote.html', context)