from django.contrib import admin

# Register your models here.
from PCS_system.models import Student, Project, Role, Permission, Role_Permission, Rating

admin.site.register(Student)
admin.site.register(Project)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(Role_Permission)
admin.site.register(Rating)
