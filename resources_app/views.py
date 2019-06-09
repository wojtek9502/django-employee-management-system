from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from resources_app import models
from resources_app import forms
from django.db.models import Q
# Create your views here.

class ResourceListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = models.ResourceModel
    paginate_by = 10
    template_name = 'resources/resource_list.html'
    context_object_name = 'resources'

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        search_query = self.request.GET.get("search_query")
        search_type = self.request.GET.get("search_type")

        if(user.is_superuser == False):
            qs = qs.filter( Q(user=user.id)  )

        if search_query is not None:
            if search_type == "name":
                qs = qs.filter( Q(name__icontains=search_query) )

        qs = qs.order_by('name')
        return qs

class ResourceCreateView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    success_url = reverse_lazy("resources_app:resources_list")

    form_class = forms.ResourceCreateForm
    
    model = models.ResourceModel
    template_name = 'resources/resource_create.html'