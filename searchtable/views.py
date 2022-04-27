from django.shortcuts import render
from data.models import *

# def corporation_in_category(request, name):
#     current_category = None
#     categories = Category.objects.all()
#     corporations = Corporation.objects.all()
#

def cor_list(request,):
    corporationLists = Corporation.objects.all()
    categories = Category.category_name

    if request.method == "POST":
        quarter = request.POST["quarter"]
        category = request.POST["category"]
        corporationList2 = corporationLists.filter(quarter=quarter)
        corporationList = corporationList2.filter(category=category)
    else:
        corporationList = corporationLists
        quarter = 'All Quarter'


    return render(request, 'searchtable/list.html', {'corporationList': corporationList, 'quarter':quarter,})


def index(request):
    return render(request, 'index.html')