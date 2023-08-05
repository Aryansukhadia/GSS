
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from home.models import Login
from home.models import Teams
from home.models import Signup
from home.models import Upcomingmatch
from home.models import Merchandise
from home.models import Ticket
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
import warnings




def booktick(request):
    if request.method == "POST":
         username =  request.POST.get('username')
         email = request.POST.get('email')
         address = request.POST.get('address')
         match = request.POST.get('match')
         quantity = request.POST.get('quantity')
        #  password =  request.POST.get('password')
         ticket = Ticket(username=username, email=email, address=address, match=match, quantity=quantity, date = datetime.today())
         ticket.save()
    return render(request, 'booktick.html')


def buy(request):
    if request.method == "POST":
         username =  request.POST.get('username')
         email = request.POST.get('email')
         address = request.POST.get('address')
         match = request.POST.get('match')
         quantity = request.POST.get('quantity')
        #  password =  request.POST.get('password')
         merchandise = Merchandise(username=username, email=email, address=address, match=match, quantity=quantity, date = datetime.today())
         merchandise.save()
    return render(request, 'buy.html')

    # return render(request, 'buy.html')

def index(request):
    return render(request, 'index.html')



def gyt(request):
    if  request.method == "POST":
        team1 =  request.POST.get('team1')
        team2 = request.POST.get('team2')
        ma_venue= request.POST.get('venue')
        ma_time= request.POST.get('time')
        ma_desc= request.POST.get('desc')
        up = Upcomingmatch(team1=team1, team2=team2, ma_venue=ma_venue, ma_time=ma_time, ma_desc=ma_desc, date = datetime.today())
        up.save()
        
    matches = Upcomingmatch.objects.all()
    matchArr = []
    count = 1
    for match in matches:
        temp ={}
        temp["id"] = count
        temp["team1"]=match.team1
        temp["team2"] = match.team2
        temp["ma_venue"] = match.ma_venue
        temp["ma_date"] = str(match.ma_date)
        temp["ma_time"] = str(match.ma_time)
        temp["ma_desc"] = match.ma_desc
        matchArr.append(temp)
        count +=1
    context = {"matches": matchArr}
    return render(request, 'gyt.html', context)

def team(request):
    return render(request, 'team.html')

def mapl(request):
    return render(request, 'mp.html')

def login(request):
    if request.method == "POST":
         username =  request.POST.get('username')
         password =  request.POST.get('password')
         login = Login(username=username, password=password, date = datetime.today())
         login.save()
    return render(request, 'login.html')
    
def mas(request):
    return render(request, 'mas.html')

def tac(request):
    return render(request, 'tac.html')

def dis(request):
    return render(request, 'disclaimer.html')

def contact(request):
    if request.method == "POST":
         name =  request.POST.get('name')
         email =  request.POST.get('email')
         subject =  request.POST.get('subject')
         message =  request.POST.get('message')
         contact = Contact(name=name, email= email, subject=subject, message=message, date = datetime.today())
         contact.save()     
    return render(request, 'contact.html')

def pripo(request):
    return render(request, 'pripo.html')


def sign(request):
        if request.method == 'POST':
             username=request.POST.get('username')
             email=request.POST.get('email')
             password=request.POST.get('password')
            #  confirmpassword=request.POST.get('confirmpassword')
             signup  = Signup(username =username, email = email, password= password, confirmpassword=password, date = datetime.today())
             signup.save()
             
        return render(request, "sign.html")
            







