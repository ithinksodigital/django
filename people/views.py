from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Buddy

def project_peeps(request):
	buddies = Buddy.objects.order_by('last_name')
	return render(request, 'people/index.html', {'buddies':buddies})
