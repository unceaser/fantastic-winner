from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import datetime

sinfo = os.uname()

def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
    response = {
            'date': datetime.now(),
            'current_page': request.path,
            'server_info': {
                'System': sinfo.sysname,
                'Hostname': sinfo.nodename,
                'Arch': sinfo.machine,
                'Vetsion':  sinfo.version
            },
            'client_info': request.META['HTTP_USER_AGENT']
    }
    return JsonResponse(response)