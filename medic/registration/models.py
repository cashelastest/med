from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

   


class Post(models.Model):
	title = models.CharField(max_length = 200)
	content = models.TextField()
	time = models.DateField(default = timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE)

class zapys(models.Model):
	name = models.CharField(max_length = 100)
	problems = models.TextField()
	date = models.DateField(null=True, blank=True)


def __str__(self):
	return self.title
# Create your models here.
