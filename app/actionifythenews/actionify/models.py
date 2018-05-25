from django.db import models

class User(models.Model):
   """Users of Actionify the News"""
   username = models.CharField(max_length=25)
   #FBID = models.ForeignKey('Facebook', on_delete=models.SET_NULL, null=True)
   #TWID = models.ForeignKey('Twitter', on_delete=models.SET_NULL, null=True)
   def __str__(self):
       """String for representing the modelTemplate"""
       return self.username

class Admin(models.Model):
   userID = models.ForeignKey('User', on_delete=models.CASCADE)

class Event(models.Model):
    eventName = models.CharField(max_length=200)
    
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

class SpamAction(models.Model):
    actionID = models.ForeignKey('Action', on_delete = models.CASCADE)
    userID = models.ForeignKey('User', on_delete = models.CASCADE)

class EventAction(models.Model):
    eventID = models.ForeignKey('Event', on_delete=models.CASCADE)
    actionID = models.ForeignKey('Action', on_delete=models.CASCADE)

class EventTag(models.Model):
    eventID = models.ForeignKey('Event', on_delete=models.CASCADE)
    tagID = models.ForeignKey('Tag', on_delete=models.CASCADE)
    
class WatchedEvent(models.Model):
    userID = models.ForeignKey('User', on_delete=models.CASCADE)
    eventID = models.ForeignKey('Event', on_delete=models.CASCADE)
    
class UserVote(models.Model):
    userID = models.ForeignKey('User', on_delete=models.CASCADE)
    actionID = models.ForeignKey('Action', on_delete=models.CASCADE)
    upvote = models.BooleanField()

