from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from courses.fields import OrderField


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
	students = models.ManyToManyField(User,
	                                  related_name='courses_joined',
	                                  blank=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.title


class Module(models.Model):
	course = models.ForeignKey(Course, models.CASCADE, related_name='modules')
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	order = OrderField(blank=True, for_fields=['course', ])
	description = models.TextField(null=True, blank=True)

	class Meta:
		ordering = ['order', ]

	def __str__(self):
		return f'{self.order}. {self.title}'


class Content(models.Model):
	module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='contents')
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={
		'model__in': ('text', 'file', 'video', 'image')
	})
	object_id = models.PositiveIntegerField()
	item = GenericForeignKey('content_type', 'object_id')
	order = OrderField(blank=True, for_fields=['module', ])

	class Meta:
		ordering = ['order', ]


class ItemBase(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_related', on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

	def __str__(self):
		return self.title


class Text(ItemBase):
	content = models.TextField()


class File(ItemBase):
	file = models.FileField(upload_to='files')


class Image(ItemBase):
	image = models.FileField(upload_to='images')


class Video(ItemBase):
	url = models.URLField()
