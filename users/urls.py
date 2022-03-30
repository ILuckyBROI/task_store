from django.urls import path
from users.views import login, UserRegistrationView, logout, profile, verify

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('logout', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('verify/<str:username>/<str:activate_key>/', verify, name='verify'),
]
