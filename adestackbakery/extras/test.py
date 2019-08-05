#from paystack_bakery_config import Paystack_bakery_conf
#import os
from recipients import Recipients
from transfers import Transfers
from utils import Utils

#os.environ['PAYSTACK_SECRET_KEY'] = "sk_test_99d432274bcb2762f94403b0a903145ce5f31476"
#os.environ['PAYSTACK_PUBLIC_KEY'] = "pk_test_d23df70a98c6efba7aab7e4b27f3a59fcc48e2da"

# Fetch Banks
#util_obj = Utils()
#res = util_obj.fetch_banks()
#print(res.json()["data"])
#print(util_obj.get_request_status(res))

# Verify Account Number
#util_obj = Utils()
#res = util_obj.verify_account_number("2081805574","057")
#print(res.json()["data"])
#print(util_obj.get_request_status(res))


# Balance Enquiry

util_obj = Utils()
res = util_obj.balance_enquiry()
print(res.json()["data"])
print(util_obj.get_request_status(res))

#recipient_obj = Recipients()

# List recipients
#res = recipient_obj.list_recipients()
#print(res.json()["data"])
#print(recipient_obj.output(res))

# Create Recipients

#req = recipient_obj.create_recipient("Adeolu Adeyemi","3048793495","011","Test account 5")
#print(req.json()["message"])

# Update Recipients
#req = recipient_obj.update_recipient("2371478", "ChangedToAdeolu","adeolu@sholaadeyemi.com")
#print(req.json()["message"])

# Delete Recipients
#req = recipient_obj.delete_recipient("2371478")
#print(recipient_obj.output(req))

# Initiate Transfer 
#trans_obj = Transfers()
#res = trans_obj.initate_transfer("500", "Test Transfer","RCP_8b99f1n6xoobwpt")
#print(res.json()["message"])

# List Transfer
#trans_obj = Transfers()
#res = trans_obj.list_transfers()
#print(res.json()["message"])

# Fetch Transfer
#trans_obj = Transfers()
#res = trans_obj.fetch_transfer("TRF_0xms4xl125wa6mt")
#print("{} - {}".format(res.json()["status"],res.json()["message"]))
#print(res.json()["data"])


