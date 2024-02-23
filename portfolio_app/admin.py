from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from .models import Student, Portfolio, Project

class MyAdminSite(admin.AdminSite):
    site_header = "Python administration"
    site_title = "Python admin"

admin_site = MyAdminSite(name="admin")
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass

admin_site.register(Student, StudentAdmin)
admin_site.register(Portfolio)
admin_site.register(Project)

