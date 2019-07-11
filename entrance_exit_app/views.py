from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from entrance_exit_app import models
from entrance_exit_app import forms
from django.db.models import Q

# Create your views here.
class EntranceExitListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = models.EntranceExitModel
    paginate_by = 10
    template_name = 'entrance_exit/entrance_exit_list.html'
    context_object_name = 'entrance_exit_list'

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        date_year = self.request.GET.get("search_query")
        search_type = self.request.GET.get("search_type")

        if(user.is_superuser == False):
            qs = qs.filter( Q(user=user.id) )

        if date_year is not None:
            if search_type == "year":
                qs = qs.filter( Q(start_date__icontains=date_year) | Q(end_date__icontains=date_year) )
        
        qs = qs.order_by('start_date')

        return qs