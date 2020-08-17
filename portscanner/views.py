from django.shortcuts import render
from django.http import JsonResponse
from time import sleep
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    return render(request, 'portscanner/home.html', {})

@csrf_exempt
def scan(request):
    if request.method == "POST":
        print('is_ajax: ',request.is_ajax())
        print(request.POST)
        print(request.POST.get('domain'))
        return JsonResponse({'message':'Scan started!'})

def scanStatus(request, scanId):
    if request.method == "GET":
        pass