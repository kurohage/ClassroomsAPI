from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView

from classes.models import Classroom
from .serializers import ClassroomSerializer, ClassroomDetailsSerializer, UpdateClassroomSerializer

# Create your views here.
class ClassroomList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer

class ClassroomDetails(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassroomUpdate(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = UpdateClassroomSerializer
	lookup_field = 'id' 
	lookup_url_kwarg = 'classroom_id'


class ClassroomDelete(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassroomCreate(CreateAPIView):
	serializer_class = UpdateClassroomSerializer

	def perform_create(self, serializer):
			#teacher_obj = User.objects.get(username=self.request.user)
			serializer.save(teacher=self.request.user)

