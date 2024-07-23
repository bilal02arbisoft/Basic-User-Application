from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView,PasswordChangeDoneView
from django.urls import reverse_lazy
from django.views import View
from .forms import CustomUserCreationForm, EditProfileForm


class SignUpView(View):

    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'

    def get(self, request):

        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save()
            login(request, user)

            return redirect('welcome')

        return render(request, self.template_name, {'form': form})


class ProfileEditView(View):

    form_class = EditProfileForm
    template_name = 'users/edit_profile.html'

    def get(self, request):

        form = self.form_class(instance=request.user.profile)

        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = self.form_class(request.POST, instance=request.user.profile)

        if form.is_valid():

            form.save()
            return redirect(reverse_lazy('profile_details'))

        return render(request, self.template_name, {'form': form})


class CustomPasswordChangeView(PasswordChangeView):

    template_name = 'users/password_change.html'
    success_url = reverse_lazy('password_change_done')


class CustomPasswordChangeDoneView(PasswordChangeDoneView):

    template_name = 'users/password_change_done.html'


class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:

            return redirect(reverse_lazy('welcome'))

        return super().dispatch(request, *args, **kwargs)


class CustomLogoutView(LogoutView):

    template_name = 'users/logged_out.html'


def welcome_view(request):

    return render(request, 'users/welcome.html', {'user': request.user})


def profile_details_view(request):

    profile = request.user.profile

    return render(request, 'users/profile_details.html', {'profile': profile})












