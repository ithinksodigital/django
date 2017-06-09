from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from .models import Photo

class IndexView(generic.ListView):
    template_name = 'simplegram/index.html'

    def get_queryset(self):
        return Photo.objects.all().order_by('created_date').reverse()


class PhotoAdd(CreateView):
    model = Photo
    fields = ['photo_pic']