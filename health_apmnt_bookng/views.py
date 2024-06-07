from django.shortcuts import render
from django.http import HttpResponse
from amwell.models import CustomUser
from healthtap.models import HealthTip
from practo.models import CustomUser
from zocdoc.models import CustomUser

def index(request):
    return render(request,"index.html")

def amwell(request):
    amwell = CustomUser.objects.all()
    return render(request, "amwell.html" ,{'amwell': amwell})

def healthtap(request):
    healthtap = HealthTip.objects.all()
    return render(request, "healthtap.html" ,{'healthtap': healthtap})

def practo(request):
    practo = CustomUser.objects.all()
    return render(request, "practo.html" ,{'practo': practo})

def zocdoc(request):
    zocdoc = CustomUser.objects.all()
    return render(request, "zocdoc.html" ,{'zocdoc': zocdoc})

def forms(request):
    # Your view logic here
    return render(request, 'CostumUser_form.html')