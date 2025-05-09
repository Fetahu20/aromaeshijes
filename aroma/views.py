from django.shortcuts import render
from .models import*
# Create your views here.
def home(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    context={"products":products, "categories":categories}
    return render(request,"home.html",context)

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
