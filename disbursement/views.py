import requests
from django.shortcuts import render
from adestackbakery.extras.utils import Utils
from adestackbakery.extras.recipients import Recipients
from adestackbakery.extras.transfers import Transfers
from django.utils.dateparse import parse_datetime
from django.contrib import messages

#save 9:46#
# Create your views here.

def index(request):
	return render(request, 'index.html', {})

def balance(request):

	# Balance Enquiry

	util_obj = Utils()
	res = util_obj.balance_enquiry()

	status = util_obj.get_request_status(res)
	# Check if the status of the balance enquiry call is true

	if not status[0]:
		messages.success(request, ("Error Fetching Balance!"))
	else:
		context = res.json()["data"][0]

	return render(request, 'balance.html', context)
	

def disbursements(request):
	context = {}
	return render(request,'disbursements.html',context)

def single_disbursement(request):
	context = {}
	return render(request,'single_disbursement.html',context)

def bulk_disbursements(request):
	context = {}
	return render(request,'bulk_disbursements.html',context)

def suppliers(request):

	#List recipients
	recipient_obj = Recipients()
	res = recipient_obj.list_recipients()

	status = recipient_obj.get_request_status(res)
	# Check if the status of the balance enquiry call is true

	if not status[0]:
		messages.success(request, ("Error Fetching Recipients!"))
	else:
		ws_date = res.json()["data"][0]["createdAt"]
		the_date = parse_datetime(ws_date)

		context = {"content": res.json()["data"],"date":the_date}
		print(context)

	return render(request,'suppliers.html',context)

def add_supplier(request):
	context = {}
	return render(request,'add_supplier.html',context)

def edit_supplier(request):
	context = {}
	return render(request,'edit_supplier.html',context)

def delete_supplier(request):
	context = {}
	return render(request,'delete_supplier.html',context)

def transactions(request):
	context = {}
	return render(request,'transactions_log.html',context)
