from django.contrib import admin

# Register your models here.
from .models import Post,Category, Tag
from comments.models import Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ['title','created_time','modified_time','category','author']
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)