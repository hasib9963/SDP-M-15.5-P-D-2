from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album
# Create your views here.

def add_album(request):
    if request.method == 'POST': # user post request koreche
        add_album = AlbumForm(request.POST) # user er post request data ekhane capture korlam
        if add_album.is_valid(): # post kora data gula amra valid kina check kortechi
            add_album.save() # jodi data valid hoy taile database e save korbo
            return redirect('homepage') # sob thik thakle take add author ei url e pathiye dibo
    
    else: # user normally website e gele blank form pabe
        post_form = AlbumForm()
    return render(request, 'add_album.html', {'form' : post_form})


def edit_album(request, Album_id):
    album = Album.objects.get(id= Album_id) 
    # print(post.title)
    if request.method == 'POST': # user post request koreche
        edit_album = AlbumForm(request.POST, instance=album) # user er post request data ekhane capture korlam
        if edit_album.is_valid(): # post kora data gula amra valid kina check kortechi
            edit_album.save() # jodi data valid hoy taile database e save korbo
            return redirect('homepage') # sob thik thakle take add author ei url e pathiye dibo
    else:
        edit_album = AlbumForm(instance=album)
        return render(request, 'edit_album.html', {'form' : edit_album})