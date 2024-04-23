from django.shortcuts import render
from ecommarceapp.models import Contact
from django.contrib import messages
from math import ceil
from ecommarceapp.models import Design




# Create your views here.
def index(request):
    allProds = []
    catprods = Design.objects.values('category', 'id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Design.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}

    return render(request, "index.html", params)




# 9-12 must be cmnt out after 15- line when uncomment
# def contact(request):
#     return render(request,"contact.html")
# def about(request):
#     return render(request,"about.html")


def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        desc=request.POST.get("desc")
        pnumber=request.POST.get("pnumber")
        myquery=Contact(name=name,email=email,desc=desc,phonenumber=pnumber)
        myquery.save()
        messages.info(request,"we will get back to you soon..")
        return render(request,"contact.html")
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")
