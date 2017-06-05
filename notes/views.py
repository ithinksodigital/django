from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from django.utils import timezone



def sitcky_notes(request):
	notes = Note.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
	return render(request, 'notes/notes.html', {'notes':notes})