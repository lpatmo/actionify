from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
   """Users of Actionify the News"""
   username = models.CharField(unique=True, max_length=25)
   email = models.EmailField(unique=True, max_length=255, blank=False)
   #FBID = models.ForeignKey('Facebook', on_delete=models.SET_NULL, null=True)
   #TWID = models.ForeignKey('Twitter', on_delete=models.SET_NULL, null=True)
   def __str__(self):
       """String for representing the modelTemplate"""
       return self.username

class Admin(models.Model):
   userID = models.ForeignKey('User', on_delete=models.CASCADE)

class Event(models.Model):
    eventName = models.CharField(unique=True, max_length=200)
    
    def __str__(self):
        return self.eventName

class New(models.Model):
    eventID = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True)
    URL = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.URL

class Tag(models.Model): 
    event = models.ManyToManyField('Event')
    name = models.CharField(max_length=250, default="Default Tag")
    
    def __str__(self):
        return self.name

class Action(models.Model):
    ACTION_TYPES = (
        ('petition', 'Petition'),
        ('donation', 'Donation'),
        ('vote', 'Vote'),
        ('call', 'Call'),
        ('attend_an_event', 'Attend an Event'),
        ('other', 'Other'),
    )
    actionType = models.CharField(max_length=20, choices=ACTION_TYPES, default="petition")
    actionURL = models.CharField(max_length=1000)
    votes = models.IntegerField(null=True, blank=True)
    creatorID = models.ForeignKey('User', null=True, on_delete = models.SET_NULL)
    
    def __str__(self):
        return self.actionURL

class UserAction(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    actionID = models.ForeignKey('Action', on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username + ": " + self.actionID.actionURL
    class Meta:
    	unique_together = ('user','actionID',)

class SpamAction(models.Model):
    actionID = models.ForeignKey('Action', on_delete = models.CASCADE)
    userID = models.ForeignKey('User', on_delete = models.CASCADE)
    def __str__(self):
        return self.userID.username + " marks spam: " + self.actionID.actionURL
    class Meta:
    	unique_together = ('actionID','userID',)
class EventAction(models.Model):
    eventID = models.ForeignKey('Event', on_delete=models.CASCADE)
    actionID = models.ForeignKey('Action', on_delete=models.CASCADE)
    def __str__(self):
        return self.eventID.eventName + ": " + self.actionID.actionURL
    class Meta:
    	unique_together = ('eventID','actionID',)
class EventTag(models.Model):
    eventID = models.ForeignKey('Event', on_delete=models.CASCADE)
    tagID = models.ForeignKey('Tag', on_delete=models.CASCADE)
    def __str__(self):
        return self.eventID.eventName + ": " + self.tagID.name
    class Meta:
    	unique_together = ('eventID','tagID',)
class WatchedEvent(models.Model):
    userID = models.ForeignKey('User', on_delete=models.CASCADE)
    eventID = models.ForeignKey('Event', on_delete=models.CASCADE)
    def __str__(self):
        return self.userID.username + ": " + self.eventID.eventName
    class Meta:
    	unique_together = ('userID','eventID',)
class UserVote(models.Model):
    userID = models.ForeignKey('User', on_delete=models.CASCADE)
    actionID = models.ForeignKey('Action', on_delete=models.CASCADE)
    upvote = models.BooleanField()
    def __str__(self):
        return self.userID.username + ": " +str(self.upvote)+ " " + self.actionID.actionURL
    class Meta:
    	unique_together = ('userID','actionID',)
