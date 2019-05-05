from django.shortcuts import render
from django.http import HttpResponse
import os
from silasdk import App
from silasdk import User as sila_user
from silasdk import Transaction



def index(request):
    app_private_key = '7C857662051B2C2653A317B15DAFD31C84D214BB2C013087B9F64FA885367100'
    app_handle = 'brukeco.silamoney.eth'
    silaApp = App("SANDBOX", app_private_key, app_handle)
    return HttpResponse('silaApp.app_handle')
