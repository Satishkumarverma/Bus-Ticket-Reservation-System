from django.shortcuts import render, redirect, HttpResponse
from app_version_1.models import signup
from admin_panel.models import Adminsingup, Bus_details, Booking
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


def home(request):
    context = {}
    if 'username' in request.session:
        context['email'] = request.session['email']
        context['username'] = request.session['username']
    if request.method == 'POST':
        start = request.POST.get('source')
        ende = request.POST.get('dest')
        date = request.POST.get('date')
        source = start[:1].upper() + start[1:]
        dest = ende[:1].upper() + ende[1:]
        if source != dest:
            data = {
                'source': source,
                'dest': dest,
                'date': date,
            }
            return render(request, 'bussearch.html', data)
        else:
            messages.info(request, "Source and Destination can't be same.")
            return render(request, 'home.html')

    return render(request, 'home.html', context)


def login(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if signup.objects.filter(email=email, password=password).exists():
            data = signup.objects.filter(email=email).values()
            request.session['email'] = data[0]['email']
            request.session['username'] = data[0]['name']
            context['email'] = data[0]['email']
            context['username'] = data[0]['name']
            return render(request, "home.html", context)
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')

    return render(request, 'login.html')


def logout(request):
    del request.session['username']
    return render(request, "home.html")


def signup_(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')
        if password == conf_password:
            if signup.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect('signuppage')
            else:
                my_data = signup(name=name, email=email,
                                 phone=phone, dob=dob, password=password)
                my_data.save()
                return redirect('login')
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect('signuppage')

    return render(request, 'signup.html')


def forgetpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')
        if signup.objects.filter(email=email).exists():
            if password == conf_password:
                signup.objects.filter(email=email).update(password=password)
                return render(request, 'login.html')
            else:
                messages.info(request, "Both passwords are not matching")
                return render(request, 'forgetpassword.html')
        else:
            messages.info(request, "Email does't exist")
            return render(request, 'forgetpassword.html')

    return render(request, 'forgetpassword.html')


def bookings(request):
    context = {}
    if 'username' in request.session:
        context['email'] = request.session['email']
        context['username'] = request.session['username']
    my_data = Booking.objects.filter(
        name=request.session['username'], email=request.session['email'])
    context['my_data'] = my_data
    return render(request, 'bookings.html', context)


def about(request):
    context = {}
    if 'username' in request.session:
        context['email'] = request.session['email']
        context['username'] = request.session['username']
    return render(request, 'about.html', context)


def bussearch(request):
    context = {}
    if 'username' in request.session:
        context['email'] = request.session['email']
        context['username'] = request.session['username']
    if request.method == 'GET':
        start = request.GET.get('source')
        ende = request.GET.get('dest')
        date = request.GET.get('date')
        source = start[:1].upper() + start[1:]
        dest = ende[:1].upper() + ende[1:]
        data = {
            'source': source,
            'dest': dest,
            'date': date,
        }

        if Bus_details.objects.filter(source=source, destination=dest, date=date).exists():
            my_data = Bus_details.objects.filter(
                source=source, destination=dest, date=date)
            data = {
                'my_data': my_data,
                'source': source,
                'dest': dest,
                'date': date,
            }
            return render(request, 'bussearch.html', data)
        else:
            data = {
                'source': source,
                'dest': dest,
                'date': date,
            }
            return render(request, 'bussearch.html', data)

    return render(request, 'bussearch.html', context)


def bookbus(request):
    context = {}
    if 'username' in request.session:
        context['email'] = request.session['email']
        context['username'] = request.session['username']
    busnumber = request.GET['busid']
    source = request.GET['source']
    dest = request.GET['dest']
    date = request.GET['date']
    my_bus = Bus_details.objects.get(busnumber=busnumber)
    my_data = Bus_details.objects.filter(
        source=source, destination=dest, date=date)
    context = {
        'my_bus': my_bus,
        'my_data': my_data,
        'source': source,
        'dest': dest,
        'date': date,
    }

    return render(request, 'bookbus.html', context)


def payment(request):
    context = {}
    if 'username' in request.session:
        context['email'] = request.session['email']
        context['username'] = request.session['username']
    busnumber = request.GET['busid']
    numberofseats = request.POST['numberofseats1']
    my_data = Bus_details.objects.filter(busnumber=busnumber).values()
    totalprice = int(my_data[0]['ticketprice']) * int(numberofseats)
    availableseats = int(my_data[0]['seats']) - int(numberofseats)
    context = {
        'busnumber': busnumber,
        'numberofseats': numberofseats,
        'totalprice': totalprice,
        'availableseats': availableseats,
    }

    return render(request, 'payment.html', context)


def transaction(request):
    context = {}
    if 'username' in request.session:
        context['email'] = request.session['email']
        context['username'] = request.session['username']
    name = request.session['username']
    mail = request.session['email']
    busnumber = request.GET['busid']
    availableseats = request.GET['availableseats']
    numberofseats = request.GET['numberofseats']
    totalprice = request.GET['totalprice']
    Bus_details.objects.filter(busnumber=busnumber).update(
        availableseats=availableseats)
    if request.method == 'POST':
        transactionid = request.POST.get('transactionid')
    if Bus_details.objects.filter(busnumber=busnumber).exists():
        Bus_data = Bus_details.objects.filter(busnumber=busnumber).values()
        busname = Bus_data[0]['busname']
        date = Bus_data[0]['date']
        source = Bus_data[0]['source']
        deparchertime = Bus_data[0]['deparchertime']
        destination = Bus_data[0]['destination']
        arrivaltime = Bus_data[0]['arrivaltime']
        durition = Bus_data[0]['durition']

    Booking_data = Booking(name=name, email=mail,
                           transactionid=transactionid, noseats=numberofseats, totalprice=totalprice, busname=busname, busnumber=busnumber, date=date, source=source, deparchertime=deparchertime, destination=destination, arrivaltime=arrivaltime, durition=durition, status='Pending')
    Booking_data.save()

    subject = 'Ticket Booking'
    html_content = f"<h2>Book Bus</h2><p>Hi {name},<br><br>&nbsp; &nbsp; Your Bus ticket has been successfully booked. Your Transaction ID is {transactionid}.</p><h3>Booking Details:-</h3>Bus No: {busnumber}<br>Bus Name: {busname}<br>Date: {date}<br>Source: {source}<br> Destination: {destination}<br>Deparcher Time: {deparchertime}<br>Arrival Time: {arrivaltime}<br>No of Seats: {numberofseats}<br>Total Price: Rs.{totalprice}/-<br><br><p>Thank you for booking have a safe jurney.</p>"
    text_content = f'Hi {name}, Your Bus ticket has been successfully booked.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [mail]
    msg = EmailMultiAlternatives(
        subject, text_content, from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return render(request, 'transaction.html')
