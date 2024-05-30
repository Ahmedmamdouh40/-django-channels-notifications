from django.db import models
from user.models import CustomUser

class Notification(models.Model):
     target_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='notification_target_user')
     message = models.CharField(max_length=250)
     
     def __str__(self) -> str:
          return self.message