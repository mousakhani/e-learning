from django.urls import path, include

from courses.api import views
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)

app_name = 'courses_api'
urlpatterns = [
	path('api-auth-token/', obtain_auth_token, name='auth-token'),
	# access token will be expired after 5 minutes
	path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_pair_view'),
	# refresh token will be expired after 24 hours
	path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
	path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
	path('subjects/<pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
	# path('courses/<pk>/enroll/', views.CourseEnrollView.as_view(), name='course_enroll'),
	path('', include(router.urls)),
]
