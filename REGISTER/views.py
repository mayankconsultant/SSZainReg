from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
from django.views.generic import ListView, CreateView
from .models import CUSTOMER, CustomerForm


class home(SuccessMessageMixin, CreateView):
    model = CUSTOMER
    form_class = CustomerForm
    template_name = "home.html"
    success_url = reverse_lazy("home")
    success_message = "Thank You Your Data will be verified and shall confirm you in 2 working days!!!!"


class list(ListView):
    model = CUSTOMER
    template_name = "list.html"
    queryset = CUSTOMER.objects.all()
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        context = super(list, self).get_context_data(**kwargs)
        return context
