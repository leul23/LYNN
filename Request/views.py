from django.shortcuts import render

# Create your views here.
def requests(request):
    return render (request,'Request/index.html')