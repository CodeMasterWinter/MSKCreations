from .forms import ContactForm
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError

# Create your views here.


def home(request):

    context = {

    }

    return render(request, 'MSKCreations/home.html', context)


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = request.POST['first_name']
            sender_surname = request.POST['last_name']
            subject = request.POST['subject']
            sender_email = request.POST['email']
            sender_message = request.POST['message']

            try:
                send_mail(
                    f'{subject} inquiry by {sender_name} {sender_surname}',
                    sender_message,
                    sender_email,
                    ['rhulanimogotsi@gmail.com', 'karabomogotsikm@gmail.com']
                )

                messages.success(request, 'Message sent! Expect to hear from us soon!')
                return redirect('home')
            except BadHeaderError:
                return HttpResponse('Invalid Header')
    else:
        form = ContactForm()

    context = {
        'page_title': 'Home',
        'contactForm': form,
    }

    return render(request, 'MSKCreations/index.html', context)