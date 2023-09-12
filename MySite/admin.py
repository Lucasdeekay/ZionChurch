from django.contrib import admin

from MySite.models import Student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")


admin.site.register(Student, StudentAdmin)
