from django.contrib import admin

# Register your models here.
from courses.models import Subject, Module, Course


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_fields = ('title',)
	prepopulated_fields = {'slug': ('title',)}


class ModuleTabular(admin.TabularInline):
	model = Module
	prepopulated_fields = {'slug': ('title',)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ('owner', 'subject', 'title', 'created')
	list_filter = ('created', 'subject')
	search_fields = ('overview', 'title')
	prepopulated_fields = {'slug': ('title',)}
	inlines = (ModuleTabular,)
