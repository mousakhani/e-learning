from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from courses.api.permissions import IsEnrolled
from courses.api.serializers import SubjectSerializer, CourseSerializer, CourseWithContentsSerializer
from courses.models import Subject, Course


class SubjectListView(generics.ListAPIView):
	permission_classes = [IsAuthenticated, ]
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer


class CourseEnrollView(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request, pk, format=None):
		course = get_object_or_404(Course, id=pk)
		course.students.add(request.user)
		return Response({'enrolled': True})


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticated, ]
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

	@action(detail=True, methods=['post', ],
	        permission_classes=[IsAuthenticated, ], )
	def enroll(self, request, *args, **kwargs):
		course = self.get_object()
		course.students.add(request.user)
		return Response({'enrolled': True})

	@action(detail=True, methods=['get', ], serializer_class=CourseWithContentsSerializer,
	        permission_classes=[IsAuthenticated, IsEnrolled])
	def contents(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	@action(detail=True, methods=['post', ],
	        permission_classes=[IsAuthenticated, IsEnrolled])
	def remove(self, request, *args, **kwargs):
		self.get_object().students.remove(request.user)
		return Response({'deleted': True})
