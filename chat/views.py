from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render


# Create your views here.


@login_required
def course_char_room(request, course_id):
	try:
		# retrieve course with given id joined by the current user
		course = request.user.courses_joined.get(id=course_id)
	except:
		# user is not a student of the course by the current user
		return HttpResponseForbidden('Error')
	return render(request, 'chat/room.html', {'course': course})
