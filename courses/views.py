from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from courses.models import Course


class OwnerMixin(object):
	def get_queryset(self):
		qs = super(OwnerMixin, self).get_queryset()
		return qs.filter(owner=self.request.user)


class OwnerEditMixin(object):
	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super(OwnerEditMixin, self).form_valid(form)


class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin):
	model = Course
	fields = ['subject', 'title', 'slug', 'overview']
	success_url = reverse_lazy('courses:manage_course_list')


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
	template_name = 'courses/manage/course/form.html'


class MangeCourseListView(OwnerCourseMixin, ListView):
	template_name = 'courses/manage/course/list.html'
	permission_required = 'courses.view_course'


class CourseCreateView(OwnerCourseEditMixin, CreateView):
	permission_required = 'courses.add_course'


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
	permission_required = 'courses.change_course'


class CourseDeleteView(OwnerCourseEditMixin, DeleteView):
	template_name = 'courses/manage/course/delete.html'
	permission_required = 'courses.delete_course'
