from django.core.checks import messages
from django.shortcuts import render
from newsletters.models import NewsLetterUser
from .forms import NewsLetterUserSignUpForm
from django.conf import settings
from django.template.loader import render_to_string
from django.core.email import EmailMessage

# Create your views here.

def newsletter_signup(request):
    form= NewsLetterUserSignUpForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        if NewsLetterUser.objects.filter(email=instance.email).exists():
            messages.Warning(request, 'Email already exists.')
        else:
            instance.save()
            messages.success(request, 'Hemos enviado un correo electronico asu correo, abrelo para  continuar con el entrenamiento')
            #correo electronico
            subject="libro de cocina"
            from_email=settings.EMAIL_HOST_USER
            to_email=[instance.email]

            html_templates='newslatters/email_templates/welcome.html'
            html_messages=render_to_string(html_templates)
            message=EmailMessage(subject, html_messages, from_email, to_email)

            message.content_subtype='html'
            message.send()
    
    context={
        'form': form
    }

    return render(request, 'opttin.html', context)