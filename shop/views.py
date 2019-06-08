from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'shop/index.html',{})


# check inventory and respond appropriately
#if successful deduct from inventory
def Purchase(request):
    pass