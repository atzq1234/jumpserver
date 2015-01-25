from django.db import models

from juser.models import User
from jasset.models import Asset


class Log(models.Model):
    user = models.ForeignKey(User)
    asset = models.ForeignKey(Asset)
    log_path = models.CharField(max_length=100)
    start_time = models.DateTimeField(null=True)
    pid = models.IntegerField(max_length=10)
    is_finished = models.BooleanField(default=False)
    end_time = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.log_path