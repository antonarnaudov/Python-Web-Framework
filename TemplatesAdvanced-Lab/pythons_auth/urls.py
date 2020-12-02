from django.urls import path

from pythons_auth.views import login_user, logout_user

urlpatterns = [
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
]
