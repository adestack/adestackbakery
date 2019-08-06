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


# Initialize Homepage Stats
def index(request):
	'''
	acc_bal = Preloader()
	res = acc_bal.fetch_balance()
	'''

	context = {}
	
	# Balance Enquiry
	util_obj = Utils()
	bal_res = util_obj.balance_enquiry()

	status = util_obj.get_request_status(bal_res)

	if not status[0]:
		return False
	else:
		print(bal_res)

		balance = int((bal_res.json()["data"][0]["balance"])/100)
		currency = bal_res.json()["data"][0]["currency"]

		current_balance = "{} {:,.2f}".format(currency,balance)

		context["balance"] = current_balance

	# Fetch Suppliers count
	recipient_obj = Recipients()
	sup_res = recipient_obj.list_recipients()
	status_sup_res = util_obj.get_request_status(sup_res)

	if not status_sup_res[0]:
		return False
	else:
		supplier_count = len(sup_res.json()["data"])
		print(supplier_count)
		context["number_supplier"] = supplier_count

	# Total No of Disbursements
	trans_obj = Transfers()
	total_res = trans_obj.list_transfers()
	status_total_res = util_obj.get_request_status(total_res)

	if not status_total_res[0]:
		return False
	else:
		amount = 0
		lista = total_res.json()["data"]
		for item in lista:
			amount += item['amount']
			print(amount)

		context["total_disbursements"] = "{} {:,.2f}".format("NGN",amount)

	# List Transfer
	list_trans_obj = Transfers()
	list_trans_res = list_trans_obj.list_transfers()
	#print(list_trans_res.json()["data"])
	new_list = list_trans_res.json()["data"]
	#print(new_list)
	latest_five = new_list[:5]
	print(latest_five)
	status_list_trans = util_obj.get_request_status(total_res)

	if not status_list_trans[0]:
		return False
	else:

		context["latest_five"] =  latest_five
		
	
	return render(request,'index.html',context)

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

def single_disbursement_ajax(request):
	if request.method == 'POST':
		amount = request.POST['amount']
		recipient = str(request.POST.get('recipient'))
		reason = str(request.POST.get('reason'))

		#format_amount = "{:.0f}".format(float(amount*100))
		format_amount = "{:.0f}".format(float(amount))
		format_amount = int(format_amount)

		print(format_amount)
		# Initiate Transfer
		trans_obj = Transfers()
		res = trans_obj.initate_transfer(format_amount,reason,recipient)

		trans_status = trans_obj.get_request_status(res)
		if not trans_status[0]:
			return HttpResponse(
				json.dumps({"error": trans_status[1]}),
				content_type="application/json"
				)
		else:
			response_data = {}
			response_data['status'] = 'success'
			response_data['success'] = 'Disbursements was successful!'

			return HttpResponse(
				json.dumps(response_data),
				content_type="application/json"
				)
	else:
		return HttpResponse(
			json.dumps({"status":"fail","error": "Disbursements was unsuccessful!"}),
			content_type="application/json"
			)
        
def single_disbursement(request):

        #List recipients
        recipient_obj = Recipients()
        res = recipient_obj.list_recipients()

        status = recipient_obj.get_request_status(res)
        # Check if the status of the balance enquiry call is true

        if not status[0]:
                messages.success(request, ("Error Fetchingy Recipient Details!"))

        else:
                supplier_dic = {}
                for supplier in res.json()["data"]:
                        supplier_dic.update( {supplier["recipient_code"]:supplier["name"]} )

                context = {"suppliers":supplier_dic}

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
