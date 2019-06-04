from __future__ import unicode_literals

import stripe as bongloy

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.html import escape
from django.http import HttpResponse
from django.contrib import messages

def new(request):
    return render(request, 'charge/new.html')

def charge(request):
    bongloy.Charge.create(
        amount=10000,
        currency="USD",
        source=request.POST["token"],
        description="Charge"
    )

    messages.success(request, 'Your Charge was successfully created!')

    return HttpResponseRedirect('/')

