# import os, json
from django.shortcuts import render
from django.conf import settings
from .models import User_entity
# from django.http import HttpResponse
# from home.models import User_entity, Developer
from silasdk import App
from silasdk import User as sila_user
from silasdk import EthWallet
from silasdk import Transaction


# app_private_key = 'B9*****************D0'
app_handle = 'brukenodedemo_test.app.silamoney.eth'
app = App("SANDBOX", settings.APP_PRIVATE_KEY, app_handle)

def index(request):
    app_private_key = '7C857662051B2C2653A317B15DAFD31C84D214BB2C013087B9F64FA885367100'
    app_handle = 'brukeco.silamoney.eth'
    silaApp = App("SANDBOX", app_private_key, app_handle)
    # return HttpResponse(silaApp.app_handle)
    user_obj = User_entity.objects.all()
    context = {'users': user_obj}
    return render(request, 'home/index.html', context=context)

def check_handle(request):
    if request.method == 'POST':
        handle_input = request.POST['handle']
        handle = handle_input + '.silamoney.eth'
        payload = {"user_handle": handle}
        response = sila_user.checkHandle(app, payload)
        context = {'message': response['message']}
        return render(request, 'home/index.html', context=context)
    else:
        return render(request, 'home/index.html')

def register(request):
    if request.method == 'POST':
        register_fields = request.POST.getlist('register')
        handle = register_fields[2] + '.silamoney.eth'
        wallet = EthWallet.create("saoiufsidyfoisueyfjwhgerhwebrwbebrwemnbrauxkhamewskhx")
        payload = {
            "country": "US",
            "user_handle": handle,
            "first_name": register_fields[0],
            "last_name": register_fields[1],
            "entity_name": register_fields[0] + ' ' + register_fields[1],
            "identity_value": register_fields[7],
            "phone": register_fields[10],
            "street_address_1": register_fields[3],
            "city": register_fields[4],
            "state": register_fields[5],
            "postal_code": register_fields[6],
            "crypto_address": wallet['eth_address'],
            "birthdate": register_fields[8],
            }
        response = sila_user.register(app, payload)

        user = User_entity(
            country="US",
            user_handle=handle,
            first_name=register_fields[0],
            last_name=register_fields[1],
            entity_name=register_fields[0] + ' ' + register_fields[1],
            identity_value=register_fields[7],
            phone=register_fields[10],
            street_address_1=register_fields[3],
            city=register_fields[4],
            state=register_fields[5],
            postal_code=register_fields[6],
            crypto_address=wallet['eth_address'],
            birthdate=register_fields[8],
            private_key=wallet['eth_private_key'],
            email=register_fields[9],
            )
        user.save()
        context = {
            'reference': response['reference'],
            'message': response['message'],
            'status': response['status'],
            'city': payload['city'],
            'state': payload['state'],
            'street': payload['street_address_1'],
            'zip': payload['postal_code'],
            'etheraddress': payload['crypto_address'],
            'handle': payload['user_handle'],
            }
        return render(request, 'home/index.html', context=context)
    else:
        return render(request, 'home/index.html')


def request_kyc(request):
    if request.method == 'POST':
        user_obj = User_entity.objects.latest('created_date')
        request_kyc_payload = {"user_handle": user_obj.user_handle}
        response = sila_user.requestKyc(app, request_kyc_payload, user_obj.private_key)
        print(response)
        context = {'message': response}
        return render(request, 'home/index.html', context=context)
    else:
        return render(request, 'home/index.html')


def check_kyc(request):
    if request.method == 'POST':
        user_obj = User_entity.objects.latest('created_date')
        check_kyc_payload = {"user_handle": user_obj.user_handle}
        response = sila_user.checkKyc(app, check_kyc_payload, user_obj.private_key)
        print(response)
        context = {'message': response}
        return render(request, 'home/index.html', context=context)
    else:
        return render(request, 'home/index.html')


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

