from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from webapp.models import Photo, Favorite

from accounts.models import Profile


class AddToFavorite(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, reqyest, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs['pk'])
        favorite, created = Favorite.objects.get_or_create(photo=photo, author=self.request.user)
        if created:
            favorite.save()
            return Response({'pk': favorite.pk})
        else:
            return Response({'message': 'you also added this photo to favorite'}, status=403)


class RemoveFromFavorite(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,  request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs['pk'])
        favorite = get_object_or_404(Favorite, photo=photo, author=self.request.user)
        favorite.delete()
        return Response({'message': f'you succesfuly remove this photo( pk = {kwargs["pk"]}) from your favorite'})


class FriendsApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        profile_which_will_be_added = get_object_or_404(Profile, pk=kwargs.get('pk'))
        profile = self.request.user.profile
        if profile == profile_which_will_be_added:
            return Response({"message": "Нельзя добавить себя в друзья"}, status=400)
        else:
            profile.friends.add(profile_which_will_be_added)
            return Response({"message": "Друг был доавлен"}, status=200)

    def delete(self, request, *args, **kwargs):
        profile_which_will_be_removed = get_object_or_404(Profile, pk=kwargs.get('pk'))
        profile = self.request.user.profile
        if profile == profile_which_will_be_removed:
            return Response({"message": "Нельзя удалить себя из друзей"}, status=400)
        else:
            profile.friends.remove(profile_which_will_be_removed)
            return Response({"message": "Друг был удален"}, status=200)