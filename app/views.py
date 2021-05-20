from app.models import Supplier
from django.shortcuts import render, redirect
from .models import Product, Supplier

def landingview(request):
    return render (request, "landingpage.html")

def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render (request,"suppliers.html",context)

def addsupplier(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])

def deletesupplier(request, id):
    Supplier.objects.filter(id = id).delete()
    return redirect(request.META['HTTP_REFERER'])


# PRODUCT
def productslistview(request):
    productslist = Product.objects.all()
    supplierlist = Supplier.objects.all()
    context = {'products': productslist, 'suppliers': supplierlist}
    return render (request,"products.html",context)

def addproduct(request):
    a = request.POST['productname']
    b = request.POST['packagesize']
    c = request.POST['unitprice']
    d = request.POST['unitsinstock']
    e = request.POST['supplier']
    Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, supplier =
    Supplier.objects.get(id=e)).save()
    return redirect(request.META['HTTP_REFERER'])

def deleteproduct(request, id):
    Product.objects.filter(id = id).delete()
    return redirect(request.META['HTTP_REFERER'])