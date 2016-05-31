# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import BlogPost, Categories

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'status')
    list_instances = True
    search_fields = ['title']

admin.site.register(BlogPost, BlogPostAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_in', 'update_to')
    list_display_links = ('name', 'created_in', 'update_to')
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Categories, CategoriesAdmin)
