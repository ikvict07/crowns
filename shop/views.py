from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, DeleteView
from .models import Product, Order, OrderItem
from .forms import AddQuantityForm, CheckForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .urls import *
from django.utils.decorators import method_decorator


# Create your views here.
def shop_product(request):
    return render(request, "shop/shop_product_col_3.html", locals())

@login_required(login_url=reverse_lazy('log_in'))
def shop_checkout(request):

    if request.method == 'POST':

        checkout_form = CheckForm(request.POST)
        if checkout_form.is_valid():
            phonenumber = checkout_form.cleaned_data['phonenumber']
            comments = checkout_form.cleaned_data['comments']


            if phonenumber:

                cart = Order.get_cart(request.user)
                cart.comments = comments
                cart.phonenumber = phonenumber
                cart.save()
                make_order(request)

        else:
            return redirect('checkout')
    return redirect('shop_product')

# def shop_single_product(request):
#     return render(request, "shop/shop_single_product.html", locals())

class ProductListView(ListView):
    model = Product
    template_name = 'shop/shop_product_col_3.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/shop_single_product.html'



@login_required(login_url=reverse_lazy('log_in'))
def add_item_to_cart(request, pk):
    if request.method == 'POST':
        quantity_form = AddQuantityForm(request.POST)
        if quantity_form.is_valid():
            quantity = quantity_form.cleaned_data['quantity']
            if quantity:
                cart = Order.get_cart(request.user)
                # product = Product.objects.get(pk=pk)
                product = get_object_or_404(Product, pk=pk)
                cart.orderitem_set.create(product=product,
                                          quantity=quantity,
                                          price=product.price)
                cart.save()
                return redirect('checkout')
        else:
            pass
    return redirect('shop_product')



@login_required(login_url=reverse_lazy('log_in'))
def cart_view(request):
    cart = Order.get_cart(request.user)
    items = cart.orderitem_set.all()
    context = {
        'cart': cart,
        'items': items,
    }
    return render(request, 'shop/shop_checkout.html', context)



@method_decorator(login_required, name='dispatch')
class CartDeleteItem(DeleteView):
    model = OrderItem
    template_name = 'shop/shop_checkout.html'
    success_url = reverse_lazy('checkout')

    # Проверка доступа
    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(order__user=self.request.user)
        return qs



@login_required(login_url=reverse_lazy('log_in'))
def make_order(request):
    cart = Order.get_cart(request.user)
    cart.make_order()
    return redirect('shop_product')



