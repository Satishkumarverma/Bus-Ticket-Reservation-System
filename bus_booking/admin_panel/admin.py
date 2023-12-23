from django.contrib import admin
from admin_panel.models import Adminsingup, Bus_details, Booking


class AdminsingupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address', 'password')


admin.site.register(Adminsingup, AdminsingupAdmin)


class Bus_detailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'busname', 'busnumber', 'date', 'ticketprice', 'source', 'deparchertime',
                    'destination', 'arrivaltime', 'durition', 'seats', 'availableseats', 'busimg')


admin.site.register(Bus_details, Bus_detailsAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'transactionid', 'noseats', 'totalprice', 'busname', 'busnumber',
                    'date', 'source', 'deparchertime', 'destination', 'arrivaltime', 'durition', 'status')


admin.site.register(Booking, BookingAdmin)
