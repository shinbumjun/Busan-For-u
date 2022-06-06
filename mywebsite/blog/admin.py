from django.contrib import admin
from blog.models import Category, Post

# admin 사이트에 알려주기
admin.site.register(Category)
admin.site.register(Post)