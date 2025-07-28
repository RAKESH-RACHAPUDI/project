from django.contrib import admin
from application.models import Student

# Register your models here.
class student_Admin(admin.ModelAdmin):
    list_display=['PIN','Name','Age','Branch','College']
    ordering=['PIN']

admin.site.register(Student,student_Admin)

