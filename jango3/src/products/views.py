from django.shortcuts import render
from .forms import ProductForm, RawProductForm
from .models import Product


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/product_create_view.html', context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, 'detail.html', context)

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now data is valid
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         'form': my_form
#     }
#     return render(request, 'products/product_create_view.html', context)

# def product_create_view(request):
#     # print(request.POST)
#     # print(request.GET)
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         print(title)
#     context = {}
#     return render(request, 'products/product_create_view.html', context)
