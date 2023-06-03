from django.contrib import admin
from .models import events
# Register your models here.

class event_data(admin.ModelAdmin):
    list_display = ('id','title','description','date','time','poster','duration')

# class blog_data(admin.ModelAdmin):
#     list_display = ('title','description')


# admin.site.register(contact, contact_data) 
admin.site.register(events, event_data)