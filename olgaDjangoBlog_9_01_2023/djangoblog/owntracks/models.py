from django.db import models
from django.utils.timezone import now


# Create your models here.

# class OwnTrackLog(models.Model):
class OwnTrackLog(models.Model):
    tid = models.CharField(max_length=100, null=False, verbose_name='пользователь')
    lat = models.FloatField(verbose_name='широта')
    lon = models.FloatField(verbose_name='долгота')
    created_time = models.DateTimeField('время создания', default=now)

    def __str__(self):
        return self.tid

    class Meta:
        ordering = ['created_time']
        verbose_name = "OwnTrackLogs"
        verbose_name_plural = verbose_name
        get_latest_by = 'created_time'
