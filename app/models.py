from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    course_id = models.ManyToManyField('Course', blank=True)
    def __str__(self):
        return self.username

class StudentProfile(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Course(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    student_id = models.ManyToManyField(Student, related_name='courses', blank=True)
    teacher_id = models.ManyToManyField('Teacher', related_name='courses', blank=True)
    def __str__(self):
        return self.title

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Lesson(models.Model):
    STATUS_CHOICE = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),

    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICE, default='Not Started', max_length=100)

    def __str__(self):
        return self.title