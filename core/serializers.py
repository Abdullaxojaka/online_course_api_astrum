from rest_framework import serializers
from .models import Instructor, Course, Lesson

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Email noto‘g‘ri!")
        return value

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("Boshlanish sanasi tugash sanasidan oldin bo‘lishi kerak.")
        return data

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    def validate_order(self, value):
        if value <= 0:
            raise serializers.ValidationError("Tartib raqami musbat bo‘lishi kerak.")
        return value
