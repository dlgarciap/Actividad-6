from django.contrib import admin
from .models import Publisher, Authorizer, Article, Comment

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'email')
    search_fields = ('first_name', 'last_name', 'student_id')

@admin.register(Authorizer)
class AuthorizerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'email')
    search_fields = ('first_name', 'last_name', 'student_id')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'authorizer', 'status', 'published_at')
    list_filter = ('status', 'publisher', 'authorizer')
    search_fields = ('title', 'content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenter_name', 'article', 'created_at')
    search_fields = ('commenter_name', 'text')