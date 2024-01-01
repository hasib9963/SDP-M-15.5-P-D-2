from django.shortcuts import render, redirect
from .forms import MusicianForm
from .models import Musician

def add_musician(request):
    if request.method == 'POST':
        add_form = MusicianForm(request.POST) 
        if add_form.is_valid(): 
            add_form.save()
            return redirect('homepage')
    else: 
        add_form = MusicianForm()
    return render(request, 'add_musician.html', {'form' : add_form})


def edit_musician(request, musician_id):
    musician = Musician.objects.get(id= musician_id) 
    if request.method == 'POST': 
        edit_form =MusicianForm(request.POST, instance=musician)
        if edit_form.is_valid():
            edit_form.save() 
            return redirect('homepage')
    else:
        edit_form =MusicianForm(instance=musician) 
    return render(request, 'edit_musician.html', {'form' : edit_form})

def delete_musician(request, id):
    musician = Musician.objects.get(pk=id) 
    musician.delete()
    return redirect('homepage')
