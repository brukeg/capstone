# import os, json
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import User_entity
import json
# from home.models import User_entity, Developer
from silasdk import App
from silasdk import User as sila_user
from silasdk import EthWallet
from silasdk import Transaction

# app_private_key = 'B9*****************D0'
app_handle = 'brukenodedemo_test.app.silamoney.eth'
app = App("SANDBOX", settings.APP_PRIVATE_KEY, app_handle)


def index(request):
    user_obj = User_entity.objects.all()
    context = {'users': user_obj}
    return render(request, 'home/index.html', context=context)


def check_handle(request):
    if request.method == 'POST':
        user_obj = User_entity.objects.all()
        context = {'users': user_obj}
        handle_input = request.POST['handle']
        handle = handle_input + '.silamoney.eth'
        payload = {"user_handle": handle}
        response = sila_user.checkHandle(app, payload)
        context['message'] = response['message']
        return render(request, 'home/index.html', context=context)
    else:
        return render(request, 'home/index.html')


def register(request):
    if request.method == 'POST':
        user_obj = User_entity.objects.all()
        context = {'users': user_obj}
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

        context['reference'] = response['reference']
        context['message'] = response['message']
        context['status'] = response['status']
        context['city'] = payload['city']
        context['state'] = payload['state']
        context['street'] = payload['street_address_1']
        context['zip'] = payload['postal_code']
        context['etheraddress'] = payload['crypto_address']
        context['handle'] = payload['user_handle']
        context['full_name'] = payload['entity_name']
        return render(request, 'home/index.html', context=context)
    else:
        return render(request, 'home/index.html')


def request_kyc(request):
    user_obj = User_entity.objects.all()
    context = {'users': user_obj}
    if request.method == 'POST':
        user = request.POST['hidden-user-handle']
        user_entity = get_object_or_404(user_obj, user_handle=user)
        request_kyc_payload = {
            "user_handle": user_entity.user_handle
        }
        response = sila_user.requestKyc(app, request_kyc_payload, user_entity.private_key)
        context['message'] = response
        return render(request, 'home/index.html', context=context)
    else:
        return render(request, 'home/index.html', context=context)


def check_kyc(request):
    user_obj = User_entity.objects.all()
    context = {'users': user_obj}
    if request.method == 'POST':
        user = request.POST['hidden-user-handle']
        user_entity = get_object_or_404(user_obj, user_handle=user)
        check_kyc_payload = {
            "user_handle": user_entity.user_handle
        }
        response = sila_user.checkKyc(app, check_kyc_payload, user_entity.private_key)
        context['message'] = response
        return render(request, 'home/index.html', context=context)
    else:
        return render(request, 'home/index.html', context=context)


@csrf_exempt
def link_account(request):
    user_obj = User_entity.objects.all()
    context = {'users': user_obj}
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        user = body['hidden-user-handle']
        user_entity = get_object_or_404(user_obj, user_handle=user)
        content = body['public_token']
        link_account_payload = {
            "public_token": content,
            "user_handle": user_entity.user_handle,
        }
        response = sila_user.linkAccount(app, link_account_payload, user_entity.private_key)
        #  TODO: context is still not printing to the screen...
        context['message'] = response
        return render(request, 'home/index.html', context=context)
    else:
        return render(request, 'home/index.html', context=context)


def get_accounts(request):
    user_obj = User_entity.objects.all()
    if request.method == 'POST':
        user = request.POST['hidden-user-handle']
        user_entity = get_object_or_404(user_obj, user_handle=user)
        get_accounts_payload = {
            "user_handle": user_entity.user_handle,
        }
        response = sila_user.getAccounts(app, get_accounts_payload, user_entity.private_key)
        response = response[0]
        return render(request, 'home/index.html', {'response': response, 'users': user_obj})
    else:
        return render(request, 'home/index.html', {'users': user_obj})


def get_transactions(request):
    user_obj = User_entity.objects.all()
    context = {'users': user_obj}
    if request.method == 'POST':
        user = request.POST['hidden-user-handle']
        user_entity = get_object_or_404(user_obj, user_handle=user)
        get_transactions_payload = {
            "user_handle": user_entity.user_handle,
        }
        response = sila_user.getTransactions(app, get_transactions_payload, user_entity.private_key)
        context['message'] = response
        return render(request, 'home/index.html', context=context)
    else:
        return render(request, 'home/index.html', context=context)


def issue_sila(request):
    user_obj = User_entity.objects.all()
    context = {'users': user_obj}
    if request.method == 'POST':
        amount = float(request.POST['issue-amount'])
        user = request.POST['hidden-user-handle']
        user_entity = get_object_or_404(user_obj, user_handle=user)
        issue_sila_payload = {
            "amount": amount,
            "user_handle": user_entity.user_handle,
        }
        response = Transaction.issueSila(app, issue_sila_payload, user_entity.private_key)
        context['message'] = response
        return render(request, 'home/index.html', context=context)
    else:
        return render(request, 'home/index.html', context=context)


def transfer_sila(request):
    user_obj = User_entity.objects.all()
    context = {'users': user_obj}
    if request.method == 'POST':
        transfer = request.POST.getlist('transfer')
        user = request.POST['hidden-user-handle']
        user_entity = get_object_or_404(user_obj, user_handle=user)
        transfer_sila_payload = {
            "amount": float(transfer[0]),
            "user_handle": user_entity.user_handle,
            "destination": transfer[1] + '.silamoney.eth',
        }
        response = Transaction.transferSila(app, transfer_sila_payload, user_entity.private_key)
        context['message'] = response
        return render(request, 'home/index.html', context=context)
    else:
        return render(request, 'home/index.html', context=context)


def redeem_sila(request):
    user_obj = User_entity.objects.all()
    context = {'users': user_obj}
    if request.method == 'POST':
        redeem = float(request.POST['redeem-amount'])
        user = request.POST['hidden-user-handle']
        user_entity = get_object_or_404(user_obj, user_handle=user)
        redeem_sila_payload = {
            "amount": redeem,
            "user_handle": user_entity.user_handle,
        }
        response = Transaction.redeemSila(app, redeem_sila_payload, user_entity.private_key)
        context['message'] = response
        return render(request, 'home/index.html', context=context)
    else:
        return render(request, 'home/index.html', context=context)
