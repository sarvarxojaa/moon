from django.contrib import admin

from .models import Blog, Contact, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'create_ad', 'is_published')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'create_ad', 'is_solved')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'create_at')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)
