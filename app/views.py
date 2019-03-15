from django.shortcuts import render

# Create your views here.
from app.models import Wheel


def index(request):
    wheels = Wheel.objects.all()
    data = {
        'wheels':wheels
    }

    return render(request,'index/index.html',context=data)