from django.shortcuts import render,redirect
from adestackbakery.extras.utils import Utils
from adestackbakery.extras.recipients import Recipients
from adestackbakery.extras.transfers import Transfers
from django.utils.dateparse import parse_datetime
from django.contrib import messages
from django.http import HttpResponse
import json

#save 9:46#
# Create your views here.


# List Transfer
def index(request):
	return render(request,'index.html',{})

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

        # List Transfer
        trans_obj = Transfers()
        res = trans_obj.list_transfers()

        status = trans_obj.get_request_status(res)

        if not status[0]:
                messages.success(request, ("Error Fetching Recipients!"))
        else:
                ws_date = res.json()["data"][0]["createdAt"]
                the_date = parse_datetime(ws_date)

                context = {"content": res.json()["data"],"the_date":the_date}
                print(context)
                return render(request,'disbursements.html',context)
        
def single_disbursement(request):

        print("I got here 1")

        if request.method == 'POST':
                amount = int(request.POST['amount'])
                recipient = str(request.POST['recipient']).strip()
                reason = request.POST['reason']
                print("I got here 2")

                # Initiate Transfer
                trans_obj = Transfers()
                res = trans_obj.initate_transfer(amount,reason,recipient)
                print(res.json()["message"])
                return redirect('disbursements')

        print("I got here 3")

        #List recipients
        recipient_obj = Recipients()
        res = recipient_obj.list_recipients()
        print("I got here 4")

        status = recipient_obj.get_request_status(res)
        # Check if the status of the balance enquiry call is true
        
        print("I got here 5")

        if not status[0]:
                messages.success(request, ("Error Fetchingy Recipient Details!"))

                print("I got here 6")
        else:
                supplier_dic = {}
                for supplier in res.json()["data"]:
                        supplier_dic.update( {supplier["recipient_code"]:supplier["name"]} )

                        print("I got here 7")
                context = {"suppliers":supplier_dic}

                print("I got here 8")
                return render(request,'single_disbursement.html',context)

def bulk_disbursements(request):

        print("I got here 1")

        if request.method == 'POST':
                amount = int(request.POST['amount'])
                recipient = str(request.POST['recipient']).strip()
                reason = request.POST['reason']
                print("I got here 2")

                # Initiate Transfer
                trans_obj = Transfers()
                res = trans_obj.initate_transfer(amount,reason,recipient)
                print(res.json()["message"])
                return redirect('disbursements')

        print("I got here 3")

        #List recipients
        recipient_obj = Recipients()
        res = recipient_obj.list_recipients()
        print("I got here 4")

        status = recipient_obj.get_request_status(res)
        # Check if the status of the balance enquiry call is true
        
        print("I got here 5")

        if not status[0]:
                messages.success(request, ("Error Fetchingy Recipient Details!"))

                print("I got here 6")
        else:
                supplier_dic = {}
                for supplier in res.json()["data"]:
                        supplier_dic.update( {supplier["recipient_code"]:supplier["name"]} )

                        print("I got here 7")
                context = {"suppliers":supplier_dic}

                print("I got here 8")
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

		context = {"content": res.json()["data"],"the_date":the_date}
		
	return render(request,'suppliers.html',context)

def add_supplier_ajax(request):
	if request.method == 'POST':
		name = request.POST['name']
		account_number = request.POST.get('account_number')
		bank_code = request.POST.get('bank_code')
		description = request.POST.get('description')
		# Create Recipients
		recipient_obj = Recipients()
		req = recipient_obj.create_recipient(name,account_number,bank_code,description)

		status = recipient_obj.get_request_status(req)

		if not status[0]:
			return HttpResponse(
				json.dumps({"error": "There was an error adding the supplier"}),
				content_type="application/json"
				)
		else:
			response_data = {}
			response_data['status'] = 'success'
			response_data['success'] = 'Supplier has been successfully added!'

			return HttpResponse(
				json.dumps(response_data),
				content_type="application/json"
				)
	else:
		return HttpResponse(
			json.dumps({"status":"fail","error": "A supplier can only be added from the Add Supplier page"}),
			content_type="application/json"
			)

def add_supplier(request):

        # Fetch Banks
        util_obj = Utils()
        res = util_obj.fetch_banks()
        
        status = util_obj.get_request_status(res)

        if not status[0]:
                messages.success(request, ("Error Fetching Banks!"))
        else:
                context = {"content": res.json()["data"]}
                return render(request,'add_supplier.html',context)
  
def edit_supplier(request, id):
        if request.method == 'POST':
                
                email = request.POST['email']
                name = request.POST['name']

                # Update Recipients
                recipient_obj = Recipients()

                req = recipient_obj.update_recipient(id, name,email)

                status = recipient_obj.get_request_status(req)

                if not status[0]:
                        messages.success(request, ("Error Updating Recipient Details!"))
                else:
                        return redirect('suppliers')

def delete_supplier(request, id):
	# Delete Recipients
	recipient_obj = Recipients()
	req = recipient_obj.delete_recipient(id)

	status = recipient_obj.get_request_status(req)

	if not status[0]:
		return HttpResponse(
			json.dumps({"status":"success","error": "There was an error deleting the supplier!"}),
			content_type="application/json"
			)
	else:
		return HttpResponse(
			json.dumps({"status":"success","success": "A supplier successfully delted!"}),
			content_type="application/json"
			)
'''
def delete_supplier(request, id):

        # Delete Recipients
        recipient_obj = Recipients()
        req = recipient_obj.delete_recipient(id)

        status = recipient_obj.get_request_status(req)

        if not status[0]:
                messages.success(request, ("Error Deleting Recipient!"))
        else:
                return redirect('suppliers')
'''