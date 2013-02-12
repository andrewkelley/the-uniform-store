from django.db import models
from django.contrib.auth.models import User
from checkout.models import BaseOrderInfo

class UserProfile(BaseOrderInfo):
    user = models.ForeignKey(User, unique=True)
    stripe_id = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return 'User Profile for: ' + self.user.username

