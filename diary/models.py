import datetime
from django.db import models
from django.utils import timezone

class Diary(models.Model):
    title_text = models.CharField(max_length=100) #title
    content_text = models.CharField(max_length=1000) #content
    pub_date = models.DateTimeField(auto_now_add=True) #Auto setted

    def __str__(self):
        return self.title_text