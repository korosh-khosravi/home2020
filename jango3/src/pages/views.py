from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'contact.html', {})


def about_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'this is about me',
        'title': 'this is Title',
        'my_number': 123,
        'this_is_true': True,
        'my_list': [123, 1, 312, 'Abc'],
        'my_html': '<h1>Hello WORLD</h1>'
    }

    return render(request, 'about.html', my_context)


def social_view(request, *args, **kwargs):
    return render(request, 'social.html', {})


def base_view(request, *args, **kwargs):
    return render(request, 'base.html', {})
