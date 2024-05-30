from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Model that represents and stores the :model:`lookup.User` information.

    Fields inherited from TimeStampedActivityModel:
        - uuid: uuid4 --> a unique uuid lookup
        - created DateTime ---> Timestamp records instance creation time
        - created_by ForeignKey(:model:`account.User`.) --> the user created the instance
        - last_updated DateTime --> Timestamp records the instance last update time
        - last_updated_by ForeignKey(:model:`account.User`.) --> the last user performed
                                                                update on the instance

    Methods:
        - __str__: str --> string represntation for the model instance
    """

    mobile = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self) -> str:
        return self.username
