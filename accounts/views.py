from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Notbot,RegistrationForm
from .models import 
# Create your views here.


def account_register(request):
    



def reg_user_view(request):
    if request.method == 'POST':
        form = Users_form(request.POST)
        firm = Notbot(request.POST)
        if firm.is_valid():
            return HttpResponse('hello my little firend')
        if form.is_valid():

            u=Users_model()
            u.first_name = request.POST.get('firstname')
            u.last_name = request.POST.get('lastname')
            u.email = request.POST.get('email')
            u.username = request.POST.get('username')
            u.password = request.POST.get('password')
            
            u.save()

            return HttpResponse('Thank you')

    form = Users_form()
    firm = Notbot()

    return render(request,'reg_user.html',{'form':form,'firm':firm})