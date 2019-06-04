from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from holiday_app import models
from holiday_app import forms
from django.db.models import Q
import datetime

# Create your views here.

class HolidayListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = models.HolidayModel
    paginate_by = 10
    template_name = 'holiday/holiday_list.html'
    context_object_name = 'holiday_list'

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        date_year = self.request.GET.get("search_query")
        search_type = self.request.GET.get("search_type")

        if(user.is_superuser == False):
            qs = qs.filter( Q(user_id=user.id) )

        if date_year is not None:
            if search_type == "year":
                qs = qs.filter( Q(start_date__icontains=date_year) | Q(end_date__icontains=date_year) )

        return qs

class HolidayCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    success_url = reverse_lazy("holiday_app:holidays_list")

    form_class = forms.HolidayForm
    
    model = models.HolidayModel
    template_name = 'holiday/holiday_create.html'

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(HolidayCreateView, self).get_form_kwargs(*args, **kwargs)
        form_kwargs['user'] = self.request.user
        print(form_kwargs)
        return form_kwargs