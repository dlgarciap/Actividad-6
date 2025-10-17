from django.contrib import admin
from .models import Student, Publisher, Authorizer, Publication

admin.site.register(Student)
admin.site.register(Publisher)
admin.site.register(Authorizer)
admin.site.register(Publication)
