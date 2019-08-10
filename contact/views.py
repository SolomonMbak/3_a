from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(
                request, "Your message has been sent successfully! Expect a response from us as soon as we can.")
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            send_mail('Message Recieved!',
                      'The message you just sent to us has been recieved. Do expect a response from us soon.',
                      'no-reply@360academia.com', [email], fail_silently=False)

            return render(request, "main/index.html")
    else:
        form = ContactForm()

    template = "contact/contact.html"
    context = {
        "form": form
    }
    return render(request, template, context)
