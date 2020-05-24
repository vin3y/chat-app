from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'sender')
    receiver = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'receiver')
    message = models.CharField(max_length = 200, blank= True)
    timestamp = models.DateTimeField(auto_now_add= True)
    is_read = models.BooleanField(default= False)
    
    
    def __str__(self):
        return self.message
    
    class Meta:
        ordering = ('timestamp',) #follows the time stamp ie, shows the recent message first
    
