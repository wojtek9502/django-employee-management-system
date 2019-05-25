from django.views.generic import TemplateView, ListView
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from ems_app import models
from django.db.models import Q

# Create your views here.

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "index.html"


class ProjectsView(LoginRequiredMixin, ListView):
    model = models.ProjectModel
    paginate_by = 10
    template_name = 'projects/project_list.html'
    context_object_name = 'user_projects_list'

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        if(user.is_superuser == False):
            qs = qs.filter( Q(id_employee=user.id) | Q(id_project_pm=user.id) )
            print(user.id)
            print(qs)

        return qs
