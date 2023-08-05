from django.contrib import admin
from home.models import Contact, Login, Upcomingmatch, Teams, Signup, Ticket, Merchandise

# Register your models here.
admin.site.register(Contact)
admin.site.register(Login)
admin.site.register(Signup)
admin.site.register(Upcomingmatch)
admin.site.register(Teams)
admin.site.register(Merchandise)
admin.site.register(Ticket)
# admin.site.register(Addplayers)

