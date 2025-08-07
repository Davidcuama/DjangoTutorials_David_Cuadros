from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProductForm

class Product:
    products = [
        {'id': 1, 'name': 'TV', 'description': '4K OLED', 'price': 1200},
        {'id': 2, 'name': 'Laptop', 'description': '16 GB RAM', 'price': 899},
        {'id': 3, 'name': 'Smartphone', 'description': '64 MP camera', 'price': 699},
    ]

class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['products'] = Product.products
        return ctx

class ProductShowView(View):
    template_name = 'pages/show.html'

    def get(self, request, id):
        try:
            product = next(p for p in Product.products if p['id'] == id)
        except StopIteration:
            messages.error(request, 'Invalid product ID – redirected to home')
            return redirect('index')
        return render(request, self.template_name, {'product': product})

class ProductCreateView(View):
    template_name = 'pages/create.html'
    form_class = ProductForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_id = max(p['id'] for p in Product.products) + 1
            Product.products.append({'id': new_id, **data})
            messages.success(request, 'Product created ✅')
            return redirect('index')
        return render(request, self.template_name, {'form': form})

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'title': 'Contact – Online Store',
            'email': 'info@example.com',
            'address': '123 Fake St, Bogotá',
            'phone': '+57 601 123 4567',
        })
        return ctx
