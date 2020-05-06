from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='users-home'),
    path('profile/',views.profile,name='users-profile'), 
    path('profile-update/',views.update_profile,name='users-profile-update'),
]

