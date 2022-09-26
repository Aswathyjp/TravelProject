from django.shortcuts import render
from . models import Place
from . models import Ntable
# Create your views here.
def index(request):
    obj = Place.objects.all()
    obj1 = Ntable.objects.all()
    return render(request, 'index.html',{'result':obj, 'op':obj1})