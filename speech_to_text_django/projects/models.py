from django.db import models

class VideoStream(models.Model):
  video_id = models.IntegerField()