from django.conf.urls import url
from people import views

urlpatterns = [
	url(r'^$', views.project_peeps, name='project_peeps'),
]