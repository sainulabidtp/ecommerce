from django.shortcuts import render
from shop.models import Product
from  django.db.models import Q
# Create your views here.

def SearchResult(request):
    products=None
    query=None
    print(request.GET.get('q'),"ccccccccccc")
    if 'q'  in request.GET:
        print("bbbbbbbbbbb")

        query= request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        for prod in products:
            print(prod)
    return render(request,'search.html',{'query':query,'products':products})