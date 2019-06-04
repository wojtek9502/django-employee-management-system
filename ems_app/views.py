from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin

# Create your views here.

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

class NoPermsPage(TemplateView):
    template_name = "no_perms.html"

    
    