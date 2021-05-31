from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Basic_forms,Notbot
from .models import Basic_model
# Create your views here.

def index(request):
    
    return render(request,'index.html',{})

def basic_forms_view(request):

    if request.method == 'POST':
        form = Basic_forms(request.POST)
        firm = Notbot(request.POST)
        if firm.is_valid():
            return HttpResponse('hello my little firend')
        if form.is_valid():

            bm=Basic_model()
            bm.name = request.POST.get('eman')
            bm.email = request.POST.get('liaem')
            bm.text = request.POST.get('txet')
            bm.save()

            return HttpResponse('Thank you')

    form = Basic_forms()
    firm = Notbot()

    return render(request,'basic_forms.html',{'form':form,'firm':firm})

