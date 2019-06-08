from django.shortcuts import render,HttpResponse,reverse,HttpResponseRedirect
from django.contrib import messages
from django.db.models import F
from django.db.models import Avg
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

        receivedData=dict(request.POST)# convert to dictionary for ease of access
        item=list(receivedData['item'])
        qty = list(receivedData['qty'])

        itemSetDictionary={}
        for i in range (len(item)):
            itemSetDictionary[item[i]]=qty[i] #  generate a convinient dictionary


        # check if available in DB
        for obj in itemSetDictionary:

            if int(itemSetDictionary[obj]) >= int(Product.objects.filter(name=obj).aggregate(Avg('quantity'))['quantity__avg']):
                # due to the property of uniqueness in name, only one value will be returned. To be able to access it, find avg
                # which will still be same value and perform comparison euqal to prevents 0 stock
                messages.error(request,'Sorry but we are out of '+str(obj))
                return HttpResponseRedirect(reverse("shop:home"))# out of any item of purchase
            else:
                pass
        # all items are available. Update DB
        for obj in itemSetDictionary:
           Product.objects.filter(name=obj).update(quantity=F('quantity')-itemSetDictionary[obj])

        # after update
        messages.success(request,'Purchase complete')
        return HttpResponseRedirect(reverse("shop:confirm"))
    else:
        return HttpResponseRedirect(reverse("shop:home"))

# confirmation page
def Confirm(request):
    return render(request, 'shop/purchase_confirm.html', context={})

