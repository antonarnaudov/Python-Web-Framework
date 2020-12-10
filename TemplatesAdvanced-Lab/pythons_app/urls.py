from django.urls import path

from pythons_auth.views import wish_python, view_wishlist
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('wish/<int:pk>', wish_python, name='wish python'),
    path('wishlist/', view_wishlist, name='wish list')
]
