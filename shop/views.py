from django.shortcuts import render,HttpResponse,reverse,HttpResponseRedirect
from django.contrib import messages
from .models import *
import json
# Create your views here.

def Home(request):
    itemset= Product.objects.all() # display as default in purchase form
    itemcount=Product.objects.count # counter on cart icon
    con={
        "items": itemset,
        "count":itemcount
    }
    return render(request,'shop/index.html',context=con)


# check inventory and respond appropriately
#if successful deduct from inventory
def Purchase(request):
    if request.POST:

        return HttpResponseRedirect(reverse("shop:confirm"))
    else:
        return HttpResponseRedirect(reverse("shop:home"))


def Confirm(request):
    return render(request, 'shop/purchase_confirm.html', context={})

