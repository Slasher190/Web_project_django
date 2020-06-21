from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "var1": "this is additional",
        "var2":"this is additional too"
    }
    return render(request,"template.html",context)
    # return HttpResponse("this is homepage")

def about(request):
    # return HttpResponse("This is about the page")
    return render(request,'about.html')
def services(request):
    # return HttpResponse("this is services page")    
    return render(request,'services.html')
def contact(request):
    # return HttpResponse("this is contact")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent !!!')
    return render(request,'contact.html')



'''makemigration = create changes and store in a File
migrate = apply the pending changes created by makemigration    '''