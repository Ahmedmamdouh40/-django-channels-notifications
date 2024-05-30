from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import CustomUser

class TicketStatusEnum(models.TextChoices):
    OPEN = "open", _("Open")
    IN_PROGRESS = "in progress", _("In Progress")
    AWAITING_REVIEW = "awaiting review", _("Awaiting Review")
    ON_HOLD = "on hold", _("On Hold")
    CLOSED = "closed", _("Closed")
    REOPEN = "reopen", _("Reopen")

class Task(models.Model):
     name = models.CharField(max_length=250)
     status = models.CharField(max_length=50, choices=TicketStatusEnum.choices, default=TicketStatusEnum.OPEN)
     opened_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='task_opened_by')

     def __str__(self) -> str:
          return self.name