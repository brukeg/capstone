from django.shortcuts import render
from django.http import HttpResponse
import os, json
from home.models import User_entity, Developer
from silasdk import App
from silasdk import User as sila_user
from silasdk import Transaction
from django.conf import settings

# app_private_key = 'B9*****************D0'
app_handle = 'brukenodedemo_test.app.silamoney.eth'
app = App("SANDBOX", settings.APP_PRIVATE_KEY, app_handle)

def index(request):
    app_private_key = '7C857662051B2C2653A317B15DAFD31C84D214BB2C013087B9F64FA885367100'
    app_handle = 'brukeco.silamoney.eth'
    silaApp = App("SANDBOX", app_private_key, app_handle)
    # return HttpResponse(silaApp.app_handle)
    return render(request, 'home/index.html')


def check_handle(request):
    if request.method == 'POST':
        handle_input = request.POST['handle']
        handle = handle_input + '.silamoney.eth'
        print(handle)
        payload = {"user_handle": handle}
        response = sila_user.checkHandle(app, payload)
        print(response)
        context = {'message': response['message']}
        return render(request, 'home/index.html', context=context)
    else:
        return render(request, 'home/index.html')

def register(request):
    if request.method == 'POST':
        register_fields = request.POST.get('register', False)
        print(register_fields)
        # data = request.json
        # result = sila_user.register(app, data)
        # self.User_entity = register_fields
        return render(request, 'home/index.html')
    else:
        return render(request, 'home/index.html')


def request_kyc(request):
    data = request.json
    result = sila_user.requestKyc(app, data, data["private_key"])
    return result


def check_kyc(request):
    data = request.json
    result = sila_user.checkKyc(app, data, data["private_key"])
    return result


def link_account(request):
    pass


def get_accounts(request):
    pass


def issue_sila(request):
    pass


def transfer_sila(request):
    pass


def redeem_sila(request):
    pass


def get_transactions(request):
    pass

