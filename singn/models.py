from django.db import models
from django.utils import timezone

class OTPCode(models.Model):
    chat_id = models.CharField(max_length=100)
    code = models.CharField(max_length=6)
    expiration_time = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expiration_time
