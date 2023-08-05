"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("booktick.html", views.booktick, name='booktick'),
    path("buy.html", views.buy, name='buy'),
    path("index.html", views.index, name='home'),
    path("gyt.html", views.gyt, name='gyt'),
    path("mp.html", views.mapl, name='played'),
    path("login.html", views.login, name='login'),
    path("mas.html", views.mas, name='mac'),
    path("tac.html", views.tac, name='tac'),
    path("disclaimer.html", views.dis, name='dis'),
    path("contact.html", views.contact, name='contact'),
    path("pripo.html", views.pripo, name='pripo'),
    path("sign.html", views.sign, name='sign'),
    path("team.html", views.team, name='team'),
    # path("saveEnquiry", views.saveEnquiry, name='saveEnquiry'),
#     # path("submitcontact", )
]
