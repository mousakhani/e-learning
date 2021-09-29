from django.urls import path

from courses import views


app_name='courses'
urlpatterns = [
	path('mine/', views.MangeCourseListView.as_view(), name='manage_course_list'),
	path('create/', views.CourseCreateView.as_view(), name='course_create'),
	path('<pk>/edit/', views.CourseUpdateView.as_view(), name='course_edit'),
	path('<pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
]
