""" Models creation """
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SubmittedWebsite(models.Model):
    """ SubmittedWebsite form fields """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='uploads/websites/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)

    objects = models.Manager()