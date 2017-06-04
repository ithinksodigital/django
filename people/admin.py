from django.contrib import admin
from people.models import Buddy


class BuddyAdmin(admin.ModelAdmin): 
	list_display = ('name', 'nickname', 'last_name')

admin.site.register(Buddy, BuddyAdmin)

# Register your models here.
