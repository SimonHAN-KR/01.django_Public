from django.shortcuts import render
# from django.db.models import Q
from .models import *


def corporation_detail(request, corp_code):
    cop1 = Corporation.objects.filter(corp_code=corp_code)[0]
    cop2 = Corporation.objects.filter(corp_code=corp_code)[1]
    cop3 = Corporation.objects.filter(corp_code=corp_code)[2]
    cop4 = Corporation.objects.filter(corp_code=corp_code)[3]

    # cat1 = Category.objects.filter(category_id=category_id)

    return render(request, 'data/detail.html', {'cop1':cop1,'cop2':cop2,'cop3':cop3,'cop4':cop4})


# def category_detail(request, category_id):
#     cat1 = Category.objects.filter(category_id=category_id)[0]
#
#     return render(request, 'data/detail.html', {'cat1':cat1})