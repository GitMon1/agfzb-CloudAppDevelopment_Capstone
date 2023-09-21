from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.views import LogoutView


app_name = 'djangoapp'
urlpatterns = [
    # path for about view
    path('about/', views.about, name='about'),

    # path for contact us view
    path('contact/', views.contact, name='contact'),

    # path for profile
    path('profile/', views.profile, name='profile'),

    # path for registration
    path('registration', views.registration_request, name='registration'),

    # path for login
    path('login/', views.login_request, name='login'),

    # path for logout
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),

    # path for all_dealers
    path('all_dealers/', views.all_dealers, name='all_dealers'),

    # path for add a review view
    path('add_review/', views.add_review, name='add_review'),

    # path for dealer reviews view

    path(route='', view=views.get_dealerships, name='index'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)