from django.shortcuts import render
from django.http import HttpResponse

def config(request):
    s={
        "brand": "acer",
       "ram":"8gb",
       "harddisk":"1tb"
      }
    for i in s:
       return HttpResponse(i)