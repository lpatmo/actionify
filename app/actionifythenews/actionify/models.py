from django.db import models

##class Users(models.Model):
##    """Users of Actionify the News"""
##    username = models.CharField(max_length=25)
##    FBID = models.ForeignKey('Facebook', on_delete=models.SET_NULL, null=True) 
##    TWID = models.ForeignKey('Twitter', on_delete=models.SET_NULL, null=True)
##    def __str__(self):
##        """String for representing the modelTemplate"""
##        return self.username
##class Admins(models.Model):
##	userID = models.ForeignKey('Users', on_delete=models.CASCADE)

class Events(models.Model):
	eventname = models.CharField(max_length=200)

class News(models.Model):
	eventID = models.ForeignKey('Events', on_delete=models.SET_NULL)
	URL = models.CharField(max_length=1000)

class Tags(models.Model):
	tag = models.ManytoManyField(Events)

class Actions(models.Model):
	actiontype = models.CharField(max_length=20)
	actionURL = models.CharField(max_length=1000)
	votes = models.IntegerField()
	creatorID = models.ForeignKey('Users', on_delete = models.SET_NULL)

class SpamActions(models.Model):
	actionID = models.ForeignKey('Actions', on_delete = models.CASCADE)
	userID = models.ForeignKey('Users', on_delete = models.CASCADE)

class EventActions(models.Model):
	eventID = models.ForeignKey('Events', on_delete=models.CASCADE)
	actionID = models.ForeignKey('Actions', on_delete=models.CASCADE)

class EventTags(models.Model):
	eventID = models.ForeignKey('Events', on_delete=models.CASCADE)
	tagID = models.ForeignKey('Tags', on_delete=models.CASCADE)
class WatchedEvents(models.Model):
	userID = models.ForeignKey('Users', on_delete=models.CASCADE)
	eventID = models.ForeignKey('Events', on_delete=models.CASCADE)
class UserVotes(models.Model):
	userID = models.ForeignKey('Users', on_delete=models.CASCADE)
	actionID = models.ForeignKey('Actions', on_delete=models.CASCADE)
	upvote = models.BooleanField()

