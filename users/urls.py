from django.urls import path

from . import views


urlpatterns = [
    # '' specifies the root
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.edit_profile, name='edit'),
]
