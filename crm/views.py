from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import *
from django.db import transaction
from .tasks import *
from .models import *
from .forms import *
from django.shortcuts import redirect

# CBVs

class index(TemplateView):
    template_name = 'index.html'

class companyCreate(CreateView):
    model = Company
    fields = ['name', 'balance']
    template_name = "create.html"
    success_url = "/"

class categoryCreate(CreateView):
    model = Category
    fields = ['name']
    template_name = "create.html"
    success_url = "/"

class stockCreate(CreateView):
    model = Stock
    fields = ["name", "price", "image", "quantity", "category", "company"]
    template_name = "create.html"
    success_url = "/"


class stockDelete(DeleteView):
    model = Stock
    template_name = "stock_confirm_delete.html"
    success_url = "/"

class stockUpdate(UpdateView):
    model = Stock
    fields = ['name', 'price', 'quantity']
    template_name = "edit.html"
    success_url = "/"

class stockList(ListView):
    model = Stock
    template_name = "list.html" 
    

class CreateTaskView(CreateView):
    model = CeleryTasks
    fields = ['message']
    template_name = "create.html"
    success_url = "taskList"

    def get_success_url(self) -> str:
        task.delay(self.object.id)
        return super().get_success_url()
    

class TaskListView(ListView):
    model = CeleryTasks
    template_name = "celery_list.html"


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