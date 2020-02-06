from django.shortcuts import render
from .forms import RequestForm
from django.http import HttpResponseRedirect

# Create your views here.
def requests(request):

    submitted = False
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            return HttpResponseRedirect('/requests?submitted=True')
    else:
        form = RequestForm()
        if 'submitted' in request.GET:
            submitted = True

    return render (request,'Request/index.html',{'form' : form , 'submitted': submitted})
    