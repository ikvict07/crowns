from django.shortcuts import render
from .forms import SubscriberForm


# Create your views here.
def index(request):
    name = 'Anton'
    form = SubscriberForm(request.POST or None)

    return render(request, 'landing/documentation.html', locals())
