from django.shortcuts import render
from MyApp.models import *
from  MyApp import forms
from django.db.models import Avg ,Max
import time
 
def index(request):
    musician_list = Musician.objects.order_by("first_name")
    diction = {
        "title":"Home",
        "musician_list":musician_list
    }
    return render(request,'MyApp/index.html',context=diction)



def album_list(request,artist_id):
    artist_info = Musician.objects.get(pk =artist_id)
    album_list = Album.objects.filter(artist = artist_id).order_by('name', 'release_date')
    artist_rating = Album.objects.filter(artist = artist_id).aggregate(Avg("num_stars"))
    diction = {
        "title":"List Of Album",
        "artist_info":artist_info,
        "album_list": album_list,
        "artist_rating": artist_rating
    }
    return render(request,'MyApp/album_list.html',context=diction)

def musician_form(request):
    form = forms.MusicianForm()
    if request.method =="POST":
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {
        "title":"Add Musician",
        'musician_form':form
    }
    return render(request,'MyApp/musician_form.html',context=diction)

def album_form(request):
        
        form = forms.AlbumForm()
        if request.method =="POST":
            form = forms.AlbumForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return index(request)
        diction = {
        "title":"Add Album",
        "album_form":form
         }
  
        return render(request,'MyApp/album_form.html',context=diction)


def edit_artist(request,artist_id):
     
     artist_info = Musician.objects.get(pk=artist_id)
     form = forms.MusicianForm(instance=artist_info)
     if request.method == "POST":
          form = forms.MusicianForm(request.POST, instance= artist_info)
          if form.is_valid():
               form.save(commit=True)
               return album_list(request,artist_id)

     diction = {
          'title':'EDIT ARTIST',
          'edit_form': form 
     }
     return render(request, 'MyApp/edit_artist.html', context=diction)



def edit_album(request,album_id):
     album_info = Album.objects.get(pk=album_id)
     form = forms.AlbumForm(instance=album_info)
     diction={}

     if request.method =="POST":
          form = forms.AlbumForm(request.POST,instance=album_info)
          if form.is_valid():
               form.save(commit=True)
               diction.update({"success_text":"Updated Successfully"})
               time.sleep(3)
               return album_list(request,album_id)
               
                
     diction.update( {
          
          'edit_form':form
     })
     diction.update({
          'album_id':album_id
     })
     return render(request, 'MyApp/edit_album.html',context=diction)

def delete(request,album_id):
     album = Album.objects.get(pk=album_id).delete()
     diction= {'delete_text':"Album deleted succesfully"}
     return render(request,'MyApp/delete.html',context=diction)

def delete_aritst(request,artist_id):
     artist = Musician.objects.get(pk=artist_id).delete()
     diction = {
          "delete_text":"Artist deleted succesfully"
     }
     return render(request,'MyApp/delete.html',context=diction)