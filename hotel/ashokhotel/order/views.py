
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage, get_connection



def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def card(request):
    return render(request,"card.html")

def contact(request):
   if request.method == "POST": 
       with get_connection(  
           host=settings.EMAIL_HOST, 
     port=settings.EMAIL_PORT,  
     username=settings.EMAIL_HOST_USER, 
     password=settings.EMAIL_HOST_PASSWORD, 
     use_tls=settings.EMAIL_USE_TLS  
       ) as connection:  
           subject = request.POST.get("subject")  
           email_from = settings.EMAIL_HOST_USER  
           recipient_list = [request.POST.get("email"), ]  
           message = request.POST.get("message")  
           EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()  
           
 
   return render(request, 'contact.html')

def menu(request):
    return render(request,"menu.html")



def reservetion(request):
    return render(request,"reservation.html")



def sucess(request):
    return HttpResponse("<h1>ashok</h1>")

# views.py
from django.shortcuts import render, redirect
from .forms import ReservationForm

def reservation_form(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success-r')
    else:
        form = ReservationForm()
    return render(request, 'reservation_form.html', {'form': form})

def success_view_r(request):
    return render(request, 'success-r.html')





# views.py
from django.shortcuts import render
from .models import Order

def order_form(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        items = ', '.join(request.POST.getlist('items'))

        order=Order( email=email, phone_number=phone_number, Name=Name, address=address, items=items)
        order.save()

        return render(request, 'success.html')

    return render(request, 'order_form.html')