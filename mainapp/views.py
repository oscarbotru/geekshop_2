import json

from django.conf import settings
from django.shortcuts import render


def index(request):
    context = {
        'custom_users': [
            {
                'name': 'Oleg Maslov'
            },
            {
                'name': 'Ivan Petrov'
            }
        ],
        'title': 'мой магазин'
    }
    return render(request, 'mainapp/index.html', context)


links_menu = [
    {'link_name': 'home', 'name': 'Дом'},
    {'link_name': 'modern', 'name': 'Модерн'},
    {'link_name': 'office', 'name': 'Офис'},
    {'link_name': 'classic', 'name': 'Классика'},
]


def products(request, name=None):
    context = {
        'links_menu': links_menu,
        'title': 'Товары'
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    with open(f'{settings.BASE_DIR}/contacts.json') as contacts_file:
        context = {
            'contacts': json.load(contacts_file)
        }
    return render(request, 'mainapp/contact.html', context)
