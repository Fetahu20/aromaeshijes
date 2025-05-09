from django.shortcuts import render
from .models import*
from django.contrib import messages
# Create your views here.
def home(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    context={"products":products, "categories":categories}
    if request.method=="POST":
       infoname=request.POST["name"]
       infoemail=request.POST["email"]
       infophone=request.POST["phone"]
       infodate=request.POST["subject"]
       infotime=request.POST["message"]
       infoguests=request.POST["message"]
       if infoname!=""and infoemail!="" and  infophone!="" and infodate!="" and infotime!="" and infoguests!="":
        Reservation(
            reservation_name=infoname,
            reservation_email=infoemail,
            reservation_phone=infophone,
            reservation_date=infodate,
            reservation_time=infotime,
            reservation_guests=infoguests,
        ).save()
        messages.success(request,"Message send!")
       else:
        messages.error(request,"Message not send!Please fill the form.")
    return render(request,"home.html",context)

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=="POST":
       infoname=request.POST["name"]
       infoemail=request.POST["email"]
       infophone=request.POST["phone"]
       infosubject=request.POST["subject"]
       infomessage=request.POST["message"]
       if infoname!=""and infoemail!="" and  infophone!="" and infosubject!="" and infomessage!="":
        Contact(
            contact_name=infoname,
            contact_email=infoemail,
            contact_phone=infophone,
            contact_subject=infosubject,
            contact_message=infomessage,
        ).save()
        messages.success(request,"Message send!")
       else:
        messages.error(request,"Message not send!Please fill the form.")

    return render(request,"contact.html")
