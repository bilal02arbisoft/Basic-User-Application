"""
URL configuration for basic_user_application project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import SignUpView, ProfileEditView, CustomPasswordChangeView, CustomLoginView, CustomLogoutView
from users.views import CustomPasswordChangeDoneView, profile_details_view, welcome_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('edit_profile/', ProfileEditView.as_view(), name='edit_profile'),
    path('profile_detail/', profile_details_view, name='profile_details'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('welcome/', welcome_view, name='welcome')

]
