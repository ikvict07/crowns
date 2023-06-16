from django.shortcuts import render
from django.views.generic import ListView
from shop.models import Product


# Create your views here.
def index_shop(request):
    return render(request, 'index/index_shop.html', locals())

class ProductListView(ListView):
    model = Product
    template_name = 'index/index_shop.html'
