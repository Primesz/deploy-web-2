from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        'judul':'Homepage'
    }
    return render(request,'index.html',context)
