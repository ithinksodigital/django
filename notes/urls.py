from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.sitcky_notes, name='sitcky_notes'),
]


