from .models import Module
from django.contrib import admin
from .models import Student
from .models import Profile
from .models import Registration

# Register your models here.

admin.site.register(Registration)
admin.site.register(Module)
admin.site.register(Profile)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'address', 'city', 'country', 'photo')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
