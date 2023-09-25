from django.shortcuts import render
from . models import food
# Create your views here.
def fun (request):
    obj=food.objects.all()
    return render(request,'index.html',{'object':obj})