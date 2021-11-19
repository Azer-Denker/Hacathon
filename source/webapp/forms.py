from django import forms
from webapp.models import Photo, Album, Jopening


class JopeningForm(forms.ModelForm):
    class Meta:
        model = Jopening
        fields = ['name', 'description']


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo_img', 'signature', 'album', 'status']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'description']
