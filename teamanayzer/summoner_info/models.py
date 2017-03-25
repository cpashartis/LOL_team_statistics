from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Summoner(models.Model):
    summoner_name_text = models.CharField(max_length=200)
    summoner_id = models.CharField(max_length=20)

    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
         return summoner_name_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

