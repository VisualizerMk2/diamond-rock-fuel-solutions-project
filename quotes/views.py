from django.shortcuts import render, redirect, get_object_or_404
from .models import FuelQuote, FuelQuoteModifier
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
  else:
    return render(request, 'pages/quote_list.html')

def get_quote(request):
  form = FuelQuoteModelForm(request.POST or None)
  user = request.user
  if form.is_valid():
    obj = form.save(commit=False) 
    obj.user = request.user
    fuel_mod_obj = get_object_or_404(FuelQuoteModifier, id=1)
    date_month = obj.delivery_date.strftime('%B')
    price_per_gallon = fuel_mod_obj.price_per_gallon
    price_per_gallon = float(price_per_gallon)
    profit_margin = float(fuel_mod_obj.profit_margin)


    # APPLY SEASON FLUCTATION
    if date_month in {'March', 'April', 'May', 'June', 'July', 'August'}:
      summer_modifier = float(fuel_mod_obj.summer_modifier)
      price_per_gallon = price_per_gallon * (1 + summer_modifier)
    
    quotes_list = FuelQuote.objects.filter(user=request.user)

    # APPLY DISCOUNTS
    if len(quotes_list) > 15:
      price_per_gallon = price_per_gallon - 0.15
      discounts = obj.gallons_requested * 0.15
    elif len(quotes_list) > 10:
      price_per_gallon = price_per_gallon - 0.10
      discounts = obj.gallons_requested * 0.10
    elif len(quotes_list) > 5:
      price_per_gallon = price_per_gallon - 0.05
      discounts = obj.gallons_requested * 0.05
    else:
      pass

    # APPLY TRANSPORTATION
    if obj.delivery_state not in {'Texas'}:
      price_per_gallon = price_per_gallon + 0.90

    # CALCULATE TOTAL AMOUNT DUE
    obj.total_amount_due = (obj.gallons_requested * price_per_gallon) * (1 + profit_margin)
    obj.price_per_gallon = price_per_gallon

    #CALCULATE TOTAL DISCOUNTS
    obj.discounts = discounts

    obj.save()
    return redirect('quotes')
  context = {
    "form": form,
    "user": user
  }
  return render(request, 'pages/get_quote.html', context)