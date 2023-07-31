from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

# displaying the Function base views(FBV means Function Base views.)

def Fbvstring(request):
    return HttpResponse('Function Base Views This is.')


# displaying The Class Base Views (CBV means Class Base Views. )

class Cbvstring(View):
    def get(self,request):
        return HttpResponse('This is Class base Views.')


# Rendering the data from Class base Views in html page. 

class Cbvtemp(View):
    def get(self,request):
        return render(request,'Cbv_first.html')