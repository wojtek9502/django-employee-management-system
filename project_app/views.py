from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from project_app import models
from project_app import forms
from django.db.models import Q

# Create your views here.

class ProjectListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = models.ProjectModel
    paginate_by = 10
    template_name = 'projects/project_list.html'
    context_object_name = 'user_projects_list'

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        search_query = self.request.GET.get("search_query")
        search_type = self.request.GET.get("search_type")

        if(user.is_superuser == False):
            qs = qs.filter( Q(id_employee=user.id) | Q(id_project_pm=user.id) )

        if search_query is not None:
            if search_type == "name":
                qs = qs.filter( Q(name__icontains=search_query) )
            if search_type == "client":
                qs = qs.filter( Q(client__icontains=search_query) )
            elif search_type == "number":
                qs = qs.filter( Q(number__icontains=search_query) | Q(number_2__icontains=search_query) )
            elif search_type == "PM":
                qs = qs.filter( Q(id_project_pm__first_name__icontains=search_query) | Q(id_project_pm__last_name__icontains=search_query) )

        qs = qs.order_by('end_date')
        return qs

class ProjectDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('accounts:login')
    model = models.ProjectModel
    context_object_name = "user_project"
    template_name = 'projects/project_detail.html'

class ProjectDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, DeleteView):
    login_url = reverse_lazy('accounts:login')
    model = models.ProjectModel
    success_url = reverse_lazy("project_app:projects_list")

    context_object_name = "user_project"
    template_name = 'projects/project_delete.html'

class ProjectUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    login_url = reverse_lazy('accounts:login')
    model = models.ProjectModel
    success_url = reverse_lazy("project_app:projects_list")

    context_object_name = "project"
    form_class = forms.ProjectForm
    template_name = 'projects/project_update.html'


class ProjectCreateView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    success_url = reverse_lazy("project_app:projects_list")

    form_class = forms.ProjectForm
    model = models.ProjectModel
    template_name = 'projects/project_create.html'


    
    