from django.shortcuts import render
from data.models import *

def rank(request):
    corporation = Corporation.objects.filter(quarter="2020년 4분기")
    corp_sales = corporation.order_by('-sales')[0:10]
    corp_op_profit = corporation.order_by('-op_profit')[0:10]
    corp_net_income = corporation.order_by('-net_income')[0:10]
    corp_PER = corporation.filter(per__gte=0.00001).order_by('per')[0:10]
    corp_PBR = corporation.filter(pbr__gte=0.00001).order_by('pbr')[0:10]
    corp_ROE = corporation.order_by('-roe')[0:10]
    return render(request, 'ranktable/rank.html',
                  {'corp_sales': corp_sales, 'corp_op_profit': corp_op_profit, 'corp_net_income': corp_net_income,
                   'corp_PER': corp_PER, 'corp_PBR': corp_PBR, 'corp_ROE': corp_ROE})