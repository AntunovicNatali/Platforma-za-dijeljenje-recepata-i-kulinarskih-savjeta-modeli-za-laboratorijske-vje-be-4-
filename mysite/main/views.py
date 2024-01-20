from django.shortcuts import render
from django.http import HttpResponse

## Create your views here.
def homepage(request):
    return HttpResponse('Dobrodošli na <strong>platformu za dijeljenje recepata i kulinarskih savjeta!</strong>')
    # primjetiti korištenje HTML-a