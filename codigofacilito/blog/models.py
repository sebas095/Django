# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import *
from tinymce import models as tinymce_models
from PIL import Image
from django.contrib.auth.models import User

ESTADO_VISIBLE = [1, 2]

class PostManager(models.Manager):
    def get_query_set(self):
        pass
        #dafault_queryset = super(PostManager, self).get_query_set()
        #return default_queryset.filter(status__in = ESTADO_VISIBLE)

class Categories(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50, unique = True, help_text = 'Esto es para la URL.')
    description = models.TextField()

    created_in = models.DateTimeField(auto_now_add = True)
    update_to = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'categories'
        ordering = ['-created_in']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

class BlogPost(models.Model):
    ESTADOS = (
        (1, "Publicado"),
        (2, "Archivado"),
        (3, "Necesita Editarse"),
        (4, "Necesita Aprobacion")
    )
    #objects_panel = models.Manager()
    #objects = PostManager()

    status = models.IntegerField(choices = ESTADOS, default = 4)
    title = models.CharField(max_length = 150)
    author = models.ForeignKey(User)
    time = models.DateTimeField()
    categories_post = models.ManyToManyField(Categories)
    image = models.ImageField(upload_to = 'photos', blank = True)
    body = tinymce_models.HTMLField()

    class Meta:
        db_table = 'inputs'
        ordering = ['-time']
        verbose_name_plural = 'Posts'

    def __unicode__(self):
        return self.title
