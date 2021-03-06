from app.models import Supplier
from django.shortcuts import render, redirect
from .models import Product, Supplier

def landingview(request):
    return render (request, "landingpage.html")

# SUPPLIER
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

def edit_supplier_get(request, id):
    supplier = Supplier.objects.filter(id = id)
    context = {'supplier': supplier}
    return render (request, "edit_supplier.html", context)

def edit_supplier_post(request, id):
    item = Supplier.objects.get(id = id)
    item.contactname = request.POST['contactname']
    item.address = request.POST['address']
    item.phone = request.POST['phone']
    item.email = request.POST['email']
    item.country = request.POST['country']
    item.save()
    return redirect(supplierlistview)


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

def edit_product_get(request, id):
    product = Product.objects.filter(id = id)
    context = {'product': product}
    return render (request, "edit_product.html", context)

def edit_product_post(request, id):
    item = Product.objects.get(id = id)
    item.unitprice = request.POST['unitprice']
    item.unitsinstock = request.POST['unitsinstock']
    item.packagesize = request.POST['packagesize']
    item.save()
    return redirect(productslistview)

def products_filtered(request, id):
    productlist = Product.objects.all()
    filteredproducts = productlist.filter(supplier = id)
    context = {'products': filteredproducts}
    return render (request,"products.html",context)