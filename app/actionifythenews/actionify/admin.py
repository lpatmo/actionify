from django.contrib import admin

# Register your models here.
from .models import Users, Admins, Events, News, Tags, Actions, SpamActions, EventActions, EventTags, WatchedEvents, UserVotes
admin.site.register(Users) 
admin.site.register(Admins) 
admin.site.register(Events) 
admin.site.register(News) 
admin.site.register(Tags) 
admin.site.register(Actions) 
admin.site.register(SpamActions) 
admin.site.register(EventActions) 
admin.site.register(EventTags) 
admin.site.register(WatchedEvents) 
admin.site.register(UserVotes)
