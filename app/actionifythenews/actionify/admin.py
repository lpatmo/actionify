from django.contrib import admin

# Regsiter your model here.
from .models import Event, New, Tag, Action, SpamAction, EventAction, EventTag, WatchedEvent, UserVote
admin.site.register(Event) 
admin.site.register(New) 
admin.site.register(Tag) 
admin.site.register(Action) 
admin.site.register(SpamAction) 
admin.site.register(EventAction) 
admin.site.register(EventTag) 
admin.site.register(WatchedEvent) 
admin.site.register(UserVote)
