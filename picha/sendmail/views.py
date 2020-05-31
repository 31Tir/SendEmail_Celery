from django.shortcuts import render, HttpResponse
from .tasks import email

def send(request):
    result = email.delay('this is subject', 'this is text for mahmood', ['example@gmail.com','layel75887@dfb55.com',])
    print(result)
    return render(request, 'index.html')
