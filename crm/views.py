from django.shortcuts import render
from django.views.generic import *

from .models import *
from .forms import *


# CBVs

class index(TemplateView):
    template_name = 'index.html'

class companyCreate(CreateView):
    model = Company
    fields = ['name', 'balance']
    template_name = "create.html"
    success_url = "/index/"

class categoryCreate(CreateView):
    model = Category
    fields = ['name']
    template_name = "create.html"
    success_url = "/index/"

class stockCreate(CreateView):
    model = Stock
    fields = ['name', 'price', 'quantity', 'category', 'company']
    template_name = "create.html"
    success_url = "/index/"


class stockDelete(DeleteView):
    model = Stock
    template_name = "stock_confirm_delete.html"
    success_url = "/list/"

class stockUpdate(UpdateView):
    model = Stock
    fields = ['name', 'price', 'quantity']
    template_name = "edit.html"
    success_url = "/index/"

class stockList(ListView):
    model = Stock
    template_name = "list.html"


#FBVs

def productSell(request):
    if request.method == "GET":
        forms = sellForms()
        return render(request, 'sell.html', context={'forms':forms})
    else:
        forms = sellForms(request.POST)
        if forms.is_valid():
            stock = forms.cleaned_data.get("product")
            quantity = forms.cleaned_data.get("quantity")


            if quantity <= stock.quantity:
                company = stock.company

                stock.quantity -= quantity
                company.balance += stock.price * quantity

                stock.save()
                company.save()

        return render(request, 'sell.html', context = {'forms': forms})