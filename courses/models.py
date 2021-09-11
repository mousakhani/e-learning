from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class Subject(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)

	class Meta:
		ordering = ('title',)

	def __str__(self):
		return self.title


class Course(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses_created')
	subject = models.ForeignKey(Subject, models.CASCADE, related_name='courses')
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	overview = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.title


class Module(models.Model):
	course = models.ForeignKey(Course, models.CASCADE, related_name='modules')
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)

	def __str__(self):
		return self.title


class Content(models.Model):
	module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='contents')
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	item = GenericForeignKey('content_type', 'object_id')
