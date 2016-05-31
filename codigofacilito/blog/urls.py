# -*- coding: utf-8 -*-
from django.conf.urls import *
from blog.views import archive, contact, thanks, contactEmail#, categories

urlpatterns = patterns('',
    url(r'^$', archive),
    url(r'^contact/', 'blog.views.contact', name = 'contact'),
    url(r'^contactEmail/', 'blog.views.contactEmail', name = 'contactEmail'),
    #url(r'^categories/', 'blog.views.categories', name = 'categories'),
    url(r'^thanks/', 'blog.views.thanks', name = 'thanks'),
)
