from django import forms

class ContactForm(forms.Form):
    mail = forms.EmailField()
    msj = forms.CharField()
    
class Form(forms.Form):
    name = forms.CharField(max_length = 100)
    msj = forms.CharField()
    mail = forms.EmailField()
