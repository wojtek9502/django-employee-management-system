from django.views.generic import TemplateView
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy, reverse

# Create your views here.

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "index.html"