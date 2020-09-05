from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import News, Calendar
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    news = News.objects.all().order_by('-date_created')[:5]
    context = {
        'news': news,
    }
    return render(request, 'mriadmin/index.html', context)


def news(request):
    news = News.objects.all().order_by('-date_created')
    paginator = Paginator(news, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'news': news,
        'page_obj': page_obj,
    }
    return render(request, 'mriadmin/news.html', context)


def calendar(request):
    events = Calendar.objects.all().order_by('-date')
    context = {
        'events': events,
    }
    return render(request, 'mriadmin/calendar.html', context)


def admission(request):
    return render(request, 'mriadmin/admission.html')


def contact(request):
    return render(request, 'mriadmin/contact.html')


def school_song(request):
    return render(request, 'mriadmin/school_song.html')


@csrf_exempt
def contact_api(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)
    firstname = data['firstname']
    lastname = data['lastname']
    email = data['email']
    phone = data['phone']
    subject = data['subject']
    mess = data['message']
    recipients = ['aathikahamed@gmail.com']

    message = f'First Name: {firstname} \nLast Name: {lastname}\nEmail Address: {email}\nPhone Number: {phone}\nSubject: {subject}\nMessage: {mess}'

    print(message, recipients)

    try:
        send_mail(subject, message, email,
                  recipients, fail_silently=True)
        print('success')

    except BadHeaderError:
        return HttpResponse('Invalid Header Found')

    return JsonResponse({"message": "Message sent successfully."}, status=201)


def about(request):
    return render(request, 'mriadmin/about.html')


def pregrade(request):
    return render(request, 'mriadmin/pregrade.html')


def primary(request):
    return render(request, 'mriadmin/primary.html')


def secondary(request):
    return render(request, 'mriadmin/secondary.html')
