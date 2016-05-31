# -*- coding: utf-8 -*-
from django.template import loader, Context, RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import BlogPost, Categories
from blog.forms import Form, ContactForm

# Create your views here.
def archive(request):
    posts = BlogPost.objects.all()
    my_template = loader.get_template("archive.html")
    my_context = Context({'posts': posts})
    return HttpResponse(my_template.render(my_context))

def contact(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/codigofacilito/blog/thanks/')
    else:
        form = Form()
        return render(request, 'contact.html', {'form': form, })

def thanks(request):
    html = '''<html>
                <body>
                  Gracias por enviarnos su comentario ...
                </body>
              </html>'''
    return HttpResponse(html)

def contactEmail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            asunto = 'Este es un mensaje de mi blog en DJANGO'
            mensaje = form.cleaned_data['msj']
            mail = EmailMessage(asunto, mensaje, to = ['sebas.duque@utp.edu.co'])
            mail.send()
        return HttpResponseRedirect('/')
    else:
        form = ContactForm()
        return render_to_response('email.html', {'form': form}, context_instance = RequestContext(request))
