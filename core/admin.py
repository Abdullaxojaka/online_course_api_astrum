from django.contrib import admin
from .models import Instructor, Course, Lesson

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'specialty')
    search_fields = ('name', 'email', 'specialty')
    list_filter = ('specialty',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'instructor', 'start_date', 'end_date')
    search_fields = ('title', 'description')
    list_filter = ('start_date', 'end_date')
    date_hierarchy = 'start_date'

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'order')
    search_fields = ('title', 'content')
    list_filter = ('course',)
    ordering = ('order',)
