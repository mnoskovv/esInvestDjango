from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import pytz

utc=pytz.UTC

# Create your models here.
class Deal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)
    term = models.PositiveIntegerField()
    summary = models.FloatField()
    percent = models.PositiveIntegerField()
    profit = models.FloatField()
    create_date = models.DateTimeField(auto_now_add = True)

    def _open_state(self):
        today = datetime.now().replace(tzinfo=utc)
        expire_date = self.create_date + timedelta(days=self.term)

        expire_date = expire_date.replace(tzinfo=utc)
        
        if (today >= expire_date):
           return False
        else:
            return True
    open_state = property(_open_state)        

    def __str__(self):
        return self.name
