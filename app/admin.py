from django.contrib import admin

from app.models import Student, Course, Teacher, Lesson
# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Lesson)

