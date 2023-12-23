from django.shortcuts import render, redirect
from admin_panel.models import Adminsingup, Bus_details, Booking
from django.contrib import messages
from datetime import datetime


def adminhome(request):
    data = {}
    if 'adminusername' in request.session:
        data['adminemail'] = request.session['adminemail']
        data['adminusername'] = request.session['adminusername']
        bus_details = Bus_details.objects.all()
        data['bus_details'] = bus_details

    return render(request, 'adminhome.html', data)


def adminlogin(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if Adminsingup.objects.filter(email=email, password=password).exists():
            data = Adminsingup.objects.filter(email=email).values()
            request.session['adminemail'] = data[0]['email']
            request.session['adminusername'] = data[0]['name']
            context['adminemail'] = data[0]['email']
            context['adminusername'] = data[0]['name']
            bus_details = Bus_details.objects.all()
            context['bus_details'] = bus_details
            return render(request, "adminhome.html", context)
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('adminlogin')

    return render(request, 'adminlogin.html')


def adminlogout(request):
    del request.session['adminusername']
    return redirect('adminlogin')


def adminsingup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')
        if password == conf_password:
            if Adminsingup.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect('adminsingup')
            else:
                my_data = Adminsingup(name=name, email=email,
                                      phone=phone, address=address, password=password)
                my_data.save()
                return redirect('adminlogin')
        else:
            messages.info(request, "Both passwords are not matching.")
            return redirect('adminsingup')

    return render(request, 'adminsingup.html')


def adminforgetpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')
        if Adminsingup.objects.filter(email=email).exists():
            if password == conf_password:
                Adminsingup.objects.filter(
                    email=email).update(password=password)
                return render(request, 'adminlogin.html')
            else:
                messages.info(request, "Both passwords are not matching")
                return render(request, 'adminforgetpassword.html')
        else:
            messages.info(request, "Email does't exist")
            return render(request, 'adminforgetpassword.html')

    return render(request, 'adminforgetpassword.html')


def adminaddbus(request):
    context = {}
    if 'adminusername' in request.session:
        context['adminemail'] = request.session['adminemail']
        context['adminusername'] = request.session['adminusername']
    if request.method == 'POST':
        busname = request.POST.get('busname')
        busnumber = request.POST.get('busnumber')
        date = request.POST.get('date')
        ticketprice = request.POST.get('ticketprice')
        source = request.POST.get('source')
        deparchertime = request.POST.get('deparchertime')
        destination = request.POST.get('destination')
        arrivaltime = request.POST.get('arrivaltime')
        seats = request.POST.get('seats')
        busimg = request.FILES['busimg']
        if Bus_details.objects.filter(busnumber=busnumber).exists():
            messages.info(request, "Bus number id already taken.")
            return redirect('adminaddbus')
        else:
            insal = 0
            deparcher = datetime.strptime(deparchertime, "%H:%M")
            arrival = datetime.strptime(arrivaltime, "%H:%M")
            totalhour = abs(int(arrival.hour) - int(deparcher.hour))
            if len(str(totalhour)) == 1:
                totalmin = f"{insal}{totalhour}"
            totalmin = abs(int(arrival.minute) - int(deparcher.minute))
            if len(str(totalmin)) == 1:
                totalmin = f"{insal}{totalmin}"
            durition = f"{totalhour}hrs:{totalmin}mins"
            bus_details = Bus_details(busname=busname, busnumber=busnumber, date=date, ticketprice=ticketprice, source=source, deparchertime=deparchertime,
                                      destination=destination, arrivaltime=arrivaltime, durition=durition, seats=seats, availableseats=seats, busimg=busimg)
            bus_details.save()
            return redirect('adminhome')
    return render(request, 'adminaddbus.html', context)


def adminupdate(request, busnumber):
    data = {}
    if 'adminusername' in request.session:
        data['adminemail'] = request.session['adminemail']
        data['adminusername'] = request.session['adminusername']
    my_data = Bus_details.objects.get(busnumber=busnumber)
    data = {
        'my_data': my_data,
    }
    if request.method == 'POST':
        busname = request.POST.get('busname')  # no change
        busnumber = request.POST.get('busnumber')  # no change
        date = request.POST.get('date')
        ticketprice = request.POST.get('ticketprice')
        source = request.POST.get('source')
        deparchertime = request.POST.get('deparchertime')
        destination = request.POST.get('destination')
        arrivaltime = request.POST.get('arrivaltime')
        seats = request.POST.get('seats')
        if Bus_details.objects.filter(busnumber=busnumber, busname=busname).exists():
            insal = 0
            deparcher = datetime.strptime(deparchertime, "%H:%M")
            arrival = datetime.strptime(arrivaltime, "%H:%M")
            totalhour = abs(int(arrival.hour) - int(deparcher.hour))
            if len(str(totalhour)) == 1:
                totalmin = f"{insal}{totalhour}"
            totalmin = abs(int(arrival.minute) - int(deparcher.minute))
            if len(str(totalmin)) == 1:
                totalmin = f"{insal}{totalmin}"
            durition = f"{totalhour}hrs:{totalmin}mins"
            Bus_details.objects.filter(busnumber=busnumber).update(date=date, ticketprice=ticketprice, source=source, deparchertime=deparchertime,
                                                                   destination=destination, arrivaltime=arrivaltime, durition=durition, seats=seats, availableseats=seats)
            return redirect('adminhome')
        else:
            messages.info(request, 'You cannot change Bus Number and Bus Name')
            return render(request, 'adminupdate.html', data)

    return render(request, 'adminupdate.html', data)


def admindeletebus(request, busnumber):
    dele = Bus_details.objects.get(busnumber=busnumber)
    dele.delete()
    return redirect('adminhome')


def adminbooking(request):
    data = {}
    if 'adminusername' in request.session:
        data['adminemail'] = request.session['adminemail']
        data['adminusername'] = request.session['adminusername']
    my_data = Booking.objects.all().order_by('-id').values()
    data['my_data'] = my_data

    return render(request, 'adminbooking.html', data)


def statusbooked(request, b_id):
    status = 'Booked'
    Booking.objects.filter(id=b_id).update(status=status)
    return redirect('adminbooking')


def statusrejected(request, b_id):
    status = 'Rejected'
    Booking.objects.filter(id=b_id).update(status=status)
    return redirect('adminbooking')
