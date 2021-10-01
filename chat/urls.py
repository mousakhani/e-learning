from django.urls import path

from chat.views import course_char_room

app_name = 'chat'
urlpatterns = [
	path('room/<int:course_id>/', course_char_room, name='room'),

]
