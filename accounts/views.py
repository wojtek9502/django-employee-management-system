from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, UpdateView
from braces.views import LoginRequiredMixin

from accounts import models
from accounts import forms

# Create your views here.
def register(request):

    registered = False

    if request.method == "POST":
        user_form = forms.UserCreateForm(data=request.POST)
        profile_form = forms.ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.is_active = True
            user.save()
            

            profile = profile_form.save(commit=False)
            # w modelu profile jest pole user z relacja 1do1 wiec uzupelniamy je
            profile.user = user
            profile.save()

            registered = True
            return redirect('accounts:after_signup')
        else:
            print(user_form.errors, profile_form.errors)

    else:  # jesli nie przeslemy nic w formularzu
        user_form = forms.UserCreateForm()
        profile_form = forms.ProfileForm()

    return render(request, 'accounts/signup.html',
                  context={'register_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})

class AfterRegisterPage(TemplateView):
    template_name = "accounts/after_signup.html"


class MyProfileTemplateView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'accounts/my_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_profile"] = models.UserProfileInfo.objects.get(user=self.request.user)
        return context


class UpdateMyProfileView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')

    model = models.UserProfileInfo
    form_class = forms.ProfileForm
    template_name = 'accounts/my_profile_update_form.html'

    def get_success_url(self):
            return reverse('index')