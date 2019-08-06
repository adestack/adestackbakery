from recipients import Recipients
from transfers import Transfers
from utils import Utils

class Preloader(Recipients,Transfers,Utils):

	def __init__(self):

		# List recipients
		recipient_obj = Recipients()
		rec_res = recipient_obj.list_recipients()

		# List Transfer
		trans_obj = Transfers()
		tran_res = trans_obj.list_transfers()

	def fetch_balance(self):

		# Balance Enquiry
		util_obj = Utils()
		bal_res = util_obj.balance_enquiry()

		status = util_obj.get_request_status(bal_res)

		if not status[0]:
			return False
		else:

			self.balance = int((res.json()["data"]["balance"])/100)
			self.currency = res.json()["data"]["currency"]

			m = Money(self.balance, self.currency)

		return m

	def verify_account_name(self, account_number, bank_code):

		util_obj = Utils()
		acc_name_res = util_obj.verify_account_number(account_number,bank_code)

		status = util_obj.get_request_status(acc_name_res)

		if not status[0]:
			return False
		else:

			self.balance = int((res.json()["data"]["balance"])/100)
			self.currency = res.json()["data"]["currency"]

			m = Money(self.balance, self.currency)

		return m

