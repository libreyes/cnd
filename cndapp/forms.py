from django import forms
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from captcha.fields import ReCaptchaField
from cndapp.models import PreOpAssessment, PreOpAssessmentVisualAcuityReading


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    def send_email(self):
        message = get_template('cndapp/message.txt')
        d = Context(self.cleaned_data)
        send_mail('Message from CND contact form', message.render(d), settings.CONTACT_SENDER,
                  settings.CONTACT_RECIPIENTS)

class CaptchaContactForm(ContactForm):
    captcha = ReCaptchaField()

class PreOpAssessmentForm(forms.ModelForm):
    class Meta:
        model = PreOpAssessment
        exclude = ( 'created_by', 'updated_by', )

PreOpAssessmentVisualAcuityReadingFormSet = forms.models.inlineformset_factory(PreOpAssessment, PreOpAssessmentVisualAcuityReading)
