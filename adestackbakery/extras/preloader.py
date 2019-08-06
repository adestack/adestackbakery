from adestackbakery.extras.recipients import Recipients
from adestackbakery.extras.transfers import Transfers
from adestackbakery.extras.utils import Utils

class Preloader(Recipients,Transfers,Utils):

	def __init__(self):

		# List recipients
		recipient_obj = Recipients()
		rec_res = recipient_obj.list_recipients()

		# List Transfer
		trans_obj = Transfers()
		tran_res = trans_obj.list_transfers()

	def fetch_balance():
		# Balance Enquiry
		util_obj = Utils()
		bal_res = util_obj.balance_enquiry()

		status = util_obj.get_request_status(bal_res)

		if not status[0]:
			return False
		else:

			balance = int((res.json()["data"]["balance"])/100)
			currency = res.json()["data"]["currency"]

			return ("{} {:,.2f}'".format(currency,balance))

	def verify_account_name(self, account_number, bank_code):

		util_obj = Utils()
		acc_name_res = util_obj.verify_account_number(account_number,bank_code)

		status = util_obj.get_request_status(acc_name_res)

		if not status[0]:
			return False
		else:

			self.balance = int((res.json()["data"]["balance"])/100)
			self.currency = res.json()["data"]["currency"]

			return ("{} {:,.2f}'".format(self.currency,self.balance))
			#m = Money(self.balance, self.currency)

		#return m

	def fetch_suppliers_count(self):
		recipient_obj = Recipients()
		sup_res = recipient_obj.list_recipients()

		status = util_obj.get_request_status(sup_res)

		if not status[0]:
			return False
		else:
			return len(res.json()["data"])

	def getTotalDisbursement(self):
		# List Transfer
		trans_obj = Transfers()
		res = trans_obj.list_transfers()

		if not status[0]:
			return False
		else:
			amount = 0
			lista = res.json()["data"]
			for item in lista:
				amount += item['amount']
				print(amount)
				return amount

	def getLastFiveDisbursement(self):
		# List Transfer
		trans_obj = Transfers()
		res = trans_obj.list_transfers()

		last_five = lista[:6]

		if not status[0]:
			return False
		else:
			last_five_list = []
			for item in last_five:
				last_five_list.append({"name":item['recipient']['name']['account_number'],
					"amount":item['amount'],
					"account_number":item['recipient']['details']['account_number']})
				return last_five_list

