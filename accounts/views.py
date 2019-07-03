from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, UpdateView, ListView
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin
from dal import autocomplete

from accounts import models
from accounts import forms

from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def register(request):

    registered = False

    if request.method == "POST":
        user_form = forms.UserCreateForm(data=request.POST)
        profile_form = forms.ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.is_active = True
            user.save()
            

            profile = profile_form.save(commit=False)
            # w modelu profile jest pole user z relacja 1do1 wiec uzupelniamy je
            profile.user = user
            profile.image = request.FILES['image'] #dołączenie zdjęcia do profiluvisual
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





#### MANGE USERS VIEWS
class UsersListView(LoginRequiredMixin, SuperuserRequiredMixin, ListView):
    login_url = reverse_lazy('accounts:login')
    model = models.UserProfileInfo
    paginate_by = 10
    context_object_name = "users_profiles_list"
    template_name = 'manage_accounts/users_list.html'

    def get_queryset(self):
        search_query = self.request.GET.get("search_query")
        search_type = self.request.GET.get("search_type")
        if search_query is not None:
            if search_type == "full_name":
                return models.UserProfileInfo.objects.filter(user__first_name__icontains=search_query) | models.UserProfileInfo.objects.filter(user__last_name__icontains=search_query)
            elif search_type == "phone":
                authors_result = models.UserProfileInfo.objects.filter(phone__icontains=search_query)
                return authors_result
            elif search_type == "pesel":
                return models.UserProfileInfo.objects.filter(pesel__icontains=search_query)
        else:
            return models.UserProfileInfo.objects.all()

class UpdateMyProfileView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')

    model = models.UserProfileInfo
    template_name = 'accounts/my_profile_update_form.html'

    #zawsze wczytany zostanie tylko obiekt usera który jest zalogowany, nie moze on edytować innych userów
    def get_object(self):
        return self.request.user.user_profile

    def get_success_url(self):
            return reverse('accounts:my_profile')


    def get_form_class(self):
        if self.request.user.is_superuser:
            return forms.ProfileForm
        else:
            return forms.ProfileUpdateForm


class UserDetailView(LoginRequiredMixin, SuperuserRequiredMixin, DetailView):
    login_url = reverse_lazy('accounts:login')
    model = models.UserProfileInfo
    context_object_name = "user_profile"
    template_name = 'manage_accounts/user_detail.html'

class UserGrantDetailView(LoginRequiredMixin, SuperuserRequiredMixin, DetailView):
    login_url = reverse_lazy('accounts:login')
    model = models.UserProfileInfo
    context_object_name = "user_profile" 
    template_name = 'manage_accounts/user_grant.html'

    def post(self, request, pk):
        userProfileInfoObj = models.UserProfileInfo.objects.get(id=pk)
        userProfileInfoObj.user.is_superuser = True
        userProfileInfoObj.user.is_staff = True
        userProfileInfoObj.user.save() 
        return redirect('accounts:users_list')


class UserGetRightsDetailView(LoginRequiredMixin, SuperuserRequiredMixin, DetailView):
    login_url = reverse_lazy('accounts:login')
    model = models.UserProfileInfo
    context_object_name = "user_profile"
    template_name = 'manage_accounts/user_get_rights.html'

    def post(self, request, pk):
        userProfileInfoObj = models.UserProfileInfo.objects.get(id=pk)
        userProfileInfoObj.user.is_superuser = False
        userProfileInfoObj.user.is_staff = False
        userProfileInfoObj.user.save()  # zapisz usera
        return redirect('accounts:users_list')

class UserActivateDetailView(LoginRequiredMixin, SuperuserRequiredMixin, DetailView):
    login_url = reverse_lazy('accounts:login')
    model = models.UserProfileInfo
    context_object_name = "user_profile"
    template_name = 'manage_accounts/user_activate.html'

    def post(self, request, pk):
        userProfileInfoObj = models.UserProfileInfo.objects.get(id=pk)
        userProfileInfoObj.user.is_active = True
        userProfileInfoObj.user.save()  # zapisz usera
        return redirect('accounts:users_list')


class UserDeactivateDetailView(LoginRequiredMixin, SuperuserRequiredMixin, DetailView):
    login_url = reverse_lazy('accounts:login')
    model = models.UserProfileInfo
    context_object_name = "user_profile"
    template_name = 'manage_accounts/user_deactivate.html'

    def post(self, request, pk):
        userProfileInfoObj = models.UserProfileInfo.objects.get(id=pk)
        userProfileInfoObj.user.is_active = False
        userProfileInfoObj.user.save()  
        return redirect('accounts:users_list')


### AUTOCOMPLETE
class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return models.MyUser.objects.none()

        qs = models.MyUser.objects.all()

        if self.q:
            qs = qs.filter(first_name__istartswith=self.q)

        return qs

class UserAdminsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return models.MyUser.objects.none()

        qs = models.MyUser.objects.filter(is_superuser=True)

        if self.q:
            qs = qs.filter(first_name__istartswith=self.q)

        return qs