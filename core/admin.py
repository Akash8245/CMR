from django.contrib import admin
from .models import Student, Teacher,Event

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "age", "branch")  # Display age & branch
    search_fields = ("username", "email", "branch")

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")
    search_fields = ("username", "email")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "is_upcoming")
    ordering = ("date",)