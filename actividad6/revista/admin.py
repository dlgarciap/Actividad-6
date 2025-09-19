from django.contrib import admin
from .models import Student, Publication, Comment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'email', 'career')
    search_fields = ('student_id','first_name','last_name','email')
    list_per_page = 25

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','authorizer','status','published_at')
    list_filter = ('status','published_at')
    search_fields = ('title','content','publisher__first_name','publisher__last_name')
    raw_id_fields = ('publisher','authorizer')
    date_hierarchy = 'published_at'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('publication', 'author', 'created_at')
    search_fields = ('content', 'author__first_name', 'author__last_name')
    list_filter = ('created_at',)
