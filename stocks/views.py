from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from .models import Stock_reading as Stocks
from datetime import date, datetime

def index(request):
    return HttpResponse("Hello, world. You're at the stocks index.")

def valid_response_insert():
    return HttpResponse('The product has successfully been inserted')

def valid_response_increase():
    return HttpResponse('The product already exists, its quantity has been raised by 1')

def create_new_reading(product_id, expiry_date):
    new_reading = Stocks()
    new_reading.product_id = product_id    
    new_reading.expiry_date = expiry_date    
    new_reading.quantity = 1    
    new_reading.ts = datetime.now()    
    new_reading.save()

def insert(request, product_id, expiry_date):
    try:
      # check that the date is in the right format
      date_obj = datetime.strptime(expiry_date, '%Y%m%d').date()
    except ValueError:
      return HttpResponseBadRequest(
        content='bad expiry date format, expecting YYYYMMDD'
      )
    # bar code of product_id is exactly 13 digits: check length
    if len(product_id) != 13:
      return HttpResponseBadRequest(
        content='bad product_id format, expecting 13 digits'
      )
    # bar code of product_id is exactly 13 digits: check only digits
    try:
      tmp = int(product_id)
    except ValueError:
      return HttpResponseBadRequest(
        content='bad product_id format, expecting 13 digits'
      )
    
    # 1st check that product does not already exist
    reading = Stocks.objects.filter(product_id=product_id).filter(expiry_date=date_obj)
    # if it exists at the same date, simply increase the quantity
    if(len(reading) > 0):
      reading[0].quantity = reading[0].quantity + 1
      reading[0].save()
      return valid_response_increase()

    # the product does not exist with the same expiry date, we need to create a new reading
    create_new_reading(product_id, date_obj)
    return valid_response_insert()

def list_current(request):
    stocks = Stocks.objects.filter(expiry_date__gte=date.today())
    context = {'stocks': stocks}
    return render(request, 'stocks/index.html', context)

def readings(request, product_id):
    stocks = Stocks.objects.filter(product_id=product_id)
    context = {'stocks': stocks}
    return render(request, 'stocks/list.html', context)

def read_closest_to_expire(request, product_id):
    earliest = Stocks.objects.filter(product_id=product_id).filter(expiry_date__gte=date.today()).earliest('expiry_date')
    return HttpResponse('the closest date is ' + str(earliest.expiry_date) + ' with a quantity of : ' + str(earliest.quantity))
