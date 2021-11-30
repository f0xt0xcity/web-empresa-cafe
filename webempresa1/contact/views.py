from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviar correo y redireccionar
            email = EmailMessage(
                "Freefire" ,
               "De {} <{}>\n\nEscribio: {}\n\n".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["manuocta@hotmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #Todo ha ido bien, redireccionar a ok
                return redirect(reverse('contact')+ "?ok")
            except:
                #Algo no ha ido bien, redireccionar a fail
                return redirect(reverse('contact')+ "?fail")

    return render(request, "contact/contact.html", {"form" : form})