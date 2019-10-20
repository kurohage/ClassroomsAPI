from rest_framework import serializers

from classes.models import Classroom


class ClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['teacher', 'subject', 'year', 'id']


class ClassroomDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['name', 'teacher', 'year', 'subject', 'id']


class UpdateClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['year', 'subject', 'name']