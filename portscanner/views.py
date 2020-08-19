from django.shortcuts import render
from django.http import JsonResponse
from time import sleep
from django.views.decorators.csrf import csrf_exempt

from urllib.parse import urlparse
from socket import gethostbyname
from ipaddress import ip_address

from .tasks import scan_job


# Create your views here.
def home(request):
    return render(request, 'portscanner/home.html', {})

@csrf_exempt
def scan(request):
    if request.method == "POST":
        domain = request.POST.get('domain')
        fastScan = request.POST.get('fastScan')
        arg = '' if fastScan else '-sV'
        print('arg: ', arg)
        if domain[0].isalpha():
            try:
                parsed = urlparse(domain)
                add = parsed.netloc if parsed.netloc!="" else parsed.path
                domain = gethostbyname(add)
            except:
                return JsonResponse({'error':'Could not parse domain name'}, status=500)
        try:
            ip_address(domain)
        except ValueError:
            return JsonResponse({'error':'Invalid IP address'}, status=500)
        print("domain to scan: ", domain)
        task = scan_job.delay(domain, arg)
        return JsonResponse({'message':'Scan started!', 'task_id':task.id, 'task_status':task.status})

def scanStatus(request, scanId):
    if request.method == "GET":
        task = scan_job.AsyncResult(scanId)
        response_data = {'task_status':task.status, 'task_id':task.id}
        if task.status == "SUCCESS":
            response_data['result'] = task.get()
        return JsonResponse(response_data)