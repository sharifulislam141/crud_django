from django.contrib import admin
from django.urls import path
from . import views

app_name = "first_app"

urlpatterns = [
    path( '',views.index, name="HomePage" ),
    path( 'add_album/',views.album_form, name="Album_Form" ),
    path( 'add_musician/',views.musician_form, name="Musician_Form" ),
    path( 'album_list/<int:artist_id>/',views.album_list, name="album_list" ),
    path( 'edit_artist/<int:artist_id>/',views.edit_artist, name="edit_artist" ),
    path( 'edit_album/<int:album_id>/',views.edit_album, name="edit_album" ),
    path( 'delete/<int:album_id>/',views.delete, name="delete" ),
    path( 'delete_artist/<int:artist_id>/',views.delete_aritst, name="delete_artist" ),


   
]
