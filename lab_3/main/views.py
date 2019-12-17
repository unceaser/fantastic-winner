from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import datetime


def main(request):
    return render(request, 'main.html', {'parameter': "kramsayu"})


def health(request):
    dt = datetime.now()
    response = {
            'date': dt.strftime("%Y-%m-%d %H:%M-%S"),
            'current_page': request.path,
            'server_info': os.uname(), 
            'client_info': request.META['HTTP_USER_AGENT']
    }
    return JsonResponse(response)

