from django.urls import path, include

from webapp.views import *

app_name = 'webapp'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo_list/', PIndexView.as_view(), name='p_index'),
    path('job/', JIndexView.as_view(), name='j_index'),

    path('jopening/', include([
        path('add/', JopeningCreateView.as_view(), name='jopening_create'),
        path('<int:pk>/', include([
            path('', JopeningView.as_view(), name='jopening_view'),
            path('update/', JopeningUpdateView.as_view(), name='jopening_update'),
            path('delete/', JopeningDeleteView.as_view(), name='jopening_delete'),
        ])),
    ])),

    path('photo/', include([
        path('add/', PhotoCreateView.as_view(), name='photo_create'),
        path('<int:pk>/', include([
            path('', PhotoView.as_view(), name='photo_view'),
            path('update/', PhotoUpdateView.as_view(), name='photo_update'),
            path('delete/', PhotoDeleteView.as_view(), name='photo_delete'),
        ])),
    ])),

    path('album/', include([
        path('add/', AlbumCreateView.as_view(), name='album_create'),
        path('<int:pk>/', include([
            path('', AlbumView.as_view(), name='album_view'),
            path('update/', AlbumUpdateView.as_view(), name='album_update'),
            path('delete/', AlbumDeleteView.as_view(), name='album_delete'),
        ])),
    ])),
]
