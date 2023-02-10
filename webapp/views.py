import random

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


# Create your views here.


def index(request: WSGIRequest):
    context = {
        'title': 'Cat',
        'name': request.POST.get('name'),
    }
    return render(request, 'webapp/index.html', context=context)


def cat_stats(request: WSGIRequest):
    if request.method == 'POST':
        context = {
            'title': 'cat stats',
            'image': 'https://avatars.mds.yandex.net/i?id=18cd75c4107164627cee70cae6d5fbbed86c1a08-7669654-images-thumbs&n=13',
            'name': '',
            'age': 1,
            'sleep': 'Now',
            'satiety_level': 55,
            'happiness_level': 15
    }
        return render(request, 'webapp/cat_stats.html', context=context)
    else:
        context = {
            'title': 'cat stats',
            'image': 'https://avatars.mds.yandex.net/i?id=6a7eb85271d8302289e051ca7bc4a2a689a012e7-8497055-images-thumbs&n=13',
            'name': request.GET.get('name'),
            'age': 1,
            'sleep': random.choice([True, False]),
            'satiety_level': 40,
            'happiness_level': 10
        }
        return render(request, 'webapp/cat_stats.html', context=context)


def stores(request):
    context = {
        'title': 'Store for Cat',
        'products': [
            {
                'image': 'https://zoopt.kz/upload/iblock/157/a2c35df2_b7b2_11eb_8118_a0d3c1f100d5_3648.jpeg',
                'name': 'Sausage Siberian',
                'price': '200',
                'description': 'Siberian sausages are a classic meat delicacy made from carefully selected veal. These sausages will please even the pickiest of pets.',
            },
            {
                'image': 'https://samizoo.ru/upload/resize_cache/iblock/8f6/480_480_0d7a58ff99b324185ccb5ad5dfbdb5e85/8f6676aaaf9059f83b70502b00f33a1d.jpeg',
                'name': 'Pillow meat',
                'price': '220',
                'description': 'The pate contained inside each pad has a soft, homogeneous texture in the form of mousse and a unique delicate taste.',
            },
            {
                'image': 'https://zoopt.kz/upload/iblock/33c/efe0df5a_1f3a_11ed_a0e4_00505601d966_5175.jpg',
                'name': 'Duck pieces',
                'price': '1200',
                'description': 'Duck Treats are a healthy treat for your pet, enriched with a general strengthening complex of vitamins A, E and D3. Net weight 40g.',
            },
        ]
    }
    return render(request, 'webapp/stores.html', context=context)
