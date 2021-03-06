from django.urls import path
from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import AddToFavorite, RemoveFromFavorite, FriendsApi

app_name = 'api'


urlpatterns = [
    path('favorites/add/<int:pk>/', AddToFavorite.as_view(), name='favorites_add'),
    path('favorites/delete/<int:pk>/', RemoveFromFavorite.as_view(), name='favorites_remove'),
    path('friends/add/<int:pk>/', FriendsApi.as_view(), name='add_to_friends'),
]
