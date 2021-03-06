import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import requests

# Create your views here.
from django.utils.crypto import get_random_string

from home.models import Setting
from order.models import ShopCart, ShopCartForm, OrderForm, Order, OrderProduct, wishList, wishListForm
from product.models import Category, Product, Variants
from user.models import UserProfile


def index(request):
    return HttpResponse("Order Page")


@login_required(login_url='/login')  # Check login
def addtoshopcart(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    product = Product.objects.get(pk=id)
    variantid = None

    if product.variant != 'None':
        variantid = request.POST.get('variantid')  # from variant add to cart
        checkinvariant = ShopCart.objects.filter(variant_id=variantid,
                                                 user_id=current_user.id)  # Check product in shopcart
        if checkinvariant:
            control = 1  # The product is in the cart
        else:
            control = 0  # The product is not in the cart"""
    else:
        checkinproduct = ShopCart.objects.filter(product_id=id, user_id=current_user.id)  # Check product in shopcart
        if checkinproduct:
            control = 1  # The product is in the cart
        else:
            control = 0  # The product is not in the cart"""

    if request.method == 'POST':  # if there is a post
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:  # Update  shopcart
                if product.variant == 'None':
                    data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
                else:
                    data = ShopCart.objects.get(product_id=id, variant_id=variantid, user_id=current_user.id)
                data.quantity += form.cleaned_data['quantity']
                data.save()  # save data
            else:  # Inser to Shopcart
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.variant_id = variantid
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "?????????? ???? ???????????? ???? ?????? ???????? ?????????? ???? ")
        return HttpResponseRedirect(url)

    else:  # if there is no post

        if control == 1:  # Update  shopcart
            data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
            data.quantity += 1
            data.save()  #
        else:  # Inser to Shopcart
            data = ShopCart()  # model ile ba??lant?? kur
            data.user_id = current_user.id
            data.product_id = id
            data.variant_id = None
            data.quantity = 1
            data.save()  #
        messages.success(request, "?????????? ???? ???????????? ???? ?????? ???????? ?????????? ????")
        return HttpResponseRedirect(url)


def shopcart(request):
    category = Category.objects.all()
    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    setting = Setting.objects.get(pk=1)
    total = 0

    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity

    transport = 0
    for rs in shopcart:
        transport += rs.product.transportation * rs.quantity

    final_total = total + transport

    amount = 0
    for rs in shopcart:
        amount += rs.quantity

    # return HttpResponse(str(total))
    context = {'shopcart': shopcart,
               'category': category,
               'total': total,
               'transport': transport,
               'final_total': final_total,
               'amount': amount,
               'setting': setting,
               }
    return render(request, 'shopcart_products.html', context)


@login_required(login_url='/login')  # Check login
def deletefromcart(request, id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "?????????? ???????? ?????? ???? ???????????? ?????? ??????????")
    return HttpResponseRedirect("/shopcart")


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
amount = 11000  # Rial / Required
description = "?????????????? ?????????? ???? ???????????? ???? ???? ?????? ???????? ???????? ????????"  # Required
email = 'p.javidan1988@gmail.com.com'  # Optional
mobile = '09101524024'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'order/orderproduct/'






def orderproduct(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity

    transport = 0
    for rs in shopcart:
        transport += rs.product.transportation * rs.quantity

    final_total = total + transport

    amount = 0
    for rs in shopcart:
        amount += rs.quantity

    if request.method == 'POST':  # if there is a post
        form = OrderForm(request.POST)
        # return HttpResponse(request.POST.items())
        if form.is_valid():
            # Send Credit card to bank,  If the bank responds ok, continue, if not, show the error

            req_data = {
                "merchant_id": MERCHANT,
                "amount": amount,
                "callback_url": CallbackURL,
                "description": description,
                "metadata": {"mobile": mobile, "email": email}
            }
            req_header = {"accept": "application/json",
                          "content-type": "application/json'"}
            req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
                req_data), headers=req_header)
            authority = req.json()['data']['authority']
            if len(req.json()['errors']) == 0:
                return redirect(ZP_API_STARTPAY.format(authority=authority))
            else:
                e_code = req.json()['errors']['code']
                e_message = req.json()['errors']['message']
                return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")

            # ..............

            data = Order()
            data.first_name = form.cleaned_data['first_name']  # get product quantity from form
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()  # random cod
            data.code = ordercode
            data.save()  #

            for rs in shopcart:
                detail = OrderProduct()
                detail.order_id = data.id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                if rs.product.variant == 'None':
                    detail.price = rs.product.price
                else:
                    detail.price = rs.variant.price
                detail.variant_id = rs.variant_id
                detail.amount = rs.amount
                detail.save()

                # ***Reduce quantity of sold product from Amount of Product
                if rs.product.variant == 'None':
                    product = Product.objects.get(id=rs.product_id)
                    product.amount -= rs.quantity
                    product.save()
                else:
                    variant = Variants.objects.get(id=rs.product_id)
                    variant.quantity -= rs.quantity
                    variant.save()
                # ************ <> *****************
            setting = Setting.objects.get(pk=1)
            ShopCart.objects.filter(user_id=current_user.id).delete()  # Clear & Delete shopcart
            request.session['cart_items'] = 0
            messages.success(request, "???????? ?????? ???? ???????????? ?????????? ????")
            return render(request, 'Order_Completed.html',
                          {'ordercode': ordercode, 'category': category, 'setting': setting, 'amount':amount})
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("/order/orderproduct")

    form = OrderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    setting = Setting.objects.get(pk=1)
    context = {'shopcart': shopcart,
               'category': category,
               'total': total,
               'form': form,
               'profile': profile,
               'transport': transport,
               'final_total': final_total,
               'setting': setting,
               'amount':amount
               }
    return render(request, 'Order_Form.html', context)








@login_required(login_url='/login')
def addtowishlist(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information

    checkinproduct = wishList.objects.filter(product_id=id)  # Check product in wishlist
    if checkinproduct:
        control = 1  # The product is in the cart
    else:
        control = 0  # The product is not in the cart"""

    if request.method == 'POST':  # if there is a post
        form = wishListForm(request.POST)
        if form.is_valid():
            if control == 1:  # Update  wishlist
                data = wishList.objects.get(product_id=id)
                data.save()  #
            else:  # Inser to wishlist
                data = wishList()  # model ile ba??lant?? kur
                data.user_id = current_user.id
                data.product_id = id
                data.save()  #
            messages.success(request, "?????????? ???? ???????????? ???? ?????????? ???????? ???? ?????????? ????")
            return HttpResponseRedirect(url)

    else:
        if control == 1:
            data = wishList.objects.get(product_id=id)
            data.save()
        else:
            data = wishList()
            data.user_id = current_user.id
            data.product_id = id
            data.save()
        messages.success(request, "?????????? ???? ???????????? ???? ?????????? ???????? ???? ?????????? ????")
        return HttpResponseRedirect(url)


def wishlist(request):
    category = Category.objects.all()
    current_user = request.user  # Access User Session information
    wishlist = wishList.objects.filter(user_id=current_user.id)
    setting = Setting.objects.get(pk=1)

    # return HttpResponse(str(total))
    context = {'wishlist': wishlist,
               'category': category,
               'setting': setting,
               }
    return render(request, 'wishlist_products.html', context)


@login_required(login_url='/login')
def deletefromwishlist(request, id):
    wishList.objects.filter(id=id).delete()
    messages.success(request, "?????????? ???????? ?????? ???? ???????????? ?????? ??????????")
    return HttpResponseRedirect("/wishlist")
