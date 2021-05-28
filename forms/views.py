from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Basic_forms
# Create your views here.

def index(request):
    
    return render(request,'index.html',{})

def basic_forms_view(request):

    if request.method == 'POST':
        form = Basic_forms(request.POST)

        if form.is_valid() and form['sun_is'] == 'yellow':
            
            
            
        

            return HttpResponse('Thank you')

    form = Basic_forms()

    return render(request,'basic_forms.html',{'form':form})
