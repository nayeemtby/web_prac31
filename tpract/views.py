import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(req):
    ctx = {
        'myString': "hello Abra'cadabra",
        'myTaggedString':'<h1>Hello World</h1>',
        'myLowerString': 'tin bela vat khai',
        'myStringSpecialChars': "<hello & Abra'cadabra />",
        'myStringMultiline': "Waku\nNaku\nLaku",
        'myInt': 678564,
        'myFloat': 5.67,
        'myArr': [1, 2, 3, 6, 4, 7, 8],
        'myDate': datetime.datetime.now(),
        'myUtc': datetime.datetime.utcfromtimestamp(0),
        'myNestedList': [1, [11, 12, 13], 2, [21, 22]],
        'myDictList': [
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
        ]
    }
    print(ctx['myUtc'])
    return render(req, 'filters.html', ctx)
