from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from entrance_exit_app import models
from resources_app.models import ResourceModel
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

class EntranceExitCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    success_url = reverse_lazy("entrance_exit_app:entrance_exit_list")

    form_class = forms.EntranceExitForm
    
    model = models.EntranceExitModel
    template_name = 'entrance_exit/entrance_exit_create.html'

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(EntranceExitCreateView, self).get_form_kwargs(*args, **kwargs)
        form_kwargs['user'] = self.request.user
        return form_kwargs

    # po utworzeniu jeśli delegacja była zatwierdzona i:
    # był podany zasób, to zmień zasób na zajęty
    def form_valid(self, form):
        response = super(EntranceExitCreateView, self).form_valid(form)
        entrance_exit_obj = self.object

        if(entrance_exit_obj.is_approved):
            for resource in entrance_exit_obj.resource.all():
                resource.is_available = False
                resource.user = self.request.user
                resource.save()

        return response

class EntranceExitDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, DeleteView):
    login_url = reverse_lazy('accounts:login')
    model = models.EntranceExitModel
    success_url = reverse_lazy("entrance_exit_app:entrance_exit_list")

    context_object_name = "entrance_exit"
    template_name = 'entrance_exit/entrance_exit_delete.html'

class EntranceExitDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('accounts:login')
    model = models.EntranceExitModel
    context_object_name = "entrance_exit"
    template_name = 'entrance_exit/entrance_exit_detail.html'

class EntranceExitUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    login_url = reverse_lazy('accounts:login')
    model = models.EntranceExitModel
    success_url = reverse_lazy("entrance_exit_app:entrance_exit_list")

    context_object_name = "entrance_exit"
    form_class = forms.EntranceExitUpdateForm
    template_name = 'entrance_exit/entrance_exit_update.html'

    # po utworzeniu jeśli delegacja była zatwierdzona i:
    # był podany zasób, to zmień zasób na zajęty
    def form_valid(self, form):
        #w ez wszystkie wcześniej zawarte w delegacji zasoby i odłącz je
        original_object = models.EntranceExitModel.objects.get(pk=self.object.pk)
        for resource_original in original_object.resource.all():
                resource_original.is_available = True
                resource_original.user = None
                resource_original.start_date = None
                resource_original.end_date = None
                resource_original.save()

        response = super(EntranceExitUpdateView, self).form_valid(form)
        new_obj = self.object
        for resource in new_obj.resource.all():
            resource.is_available = False
            resource.user = self.request.user
            resource.start_date = new_obj.start_date
            resource.end_date = new_obj.end_date
            resource.save()

        return response