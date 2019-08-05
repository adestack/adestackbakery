'''
transfer.py
'''

import requests
from adestackbakery.extras.base.base import Base

class Transfers(Base):

    amount = None
    currency = None
    source = None
    reason = None
    recipient_code = None
    transfer_code = None
    id = None
    createdAt = None
    status = None
    otp = None
    id_or_code = None
    
    def __init__(self):
        super().__init__()

        self.headers = self._header()
        self.endpoint = self._url('transfer')
    
    def initate_transfer(self, amount, reason, recipient_code, source="balance", currency="NGN"):

        self.currency = self.clean_currency(currency)
        self.amount = self.clean_amount(amount)
        self.reason = reason
        self.recipient_code = recipient_code
        self.source = source
        
        req_data = {
            "source":self.source,
            "amount":self.amount,
            "currency":self.currency,
            "reason":self.reason,
            "recipient":self.recipient_code,
            }
        
        response = requests.post(self.endpoint, data=self.build_request(req_data), headers = self.headers)

        return response

    def list_transfers(self):

        response  = requests.get(self.endpoint, headers = self.headers)

        return response

    def fetch_transfer(self, id_or_code):

        self.id_or_code = id_or_code

        response = requests.get("{}/{}".format(self.endpoint,self.id_or_code), headers = self.headers)

        return response

    def finalize_transfer(self, otp, transfer_code):

        self.otp = otp
        self.transfer_code = transfer_code

        req_data = {
            "transfer_code": self.transfer_code,
            "otp": self.otp
           }
        print(req_data)
        response = requests.post("{}/finalize_transfer".format(self.endpoint), data = self.build_request(req_data), headers = self.headers)

        return response

    def initiate_bulk_transfer(self, req_data):

        if not isinstance(req_data, dict):
            raise TypeError("data argument should be a dictionary")

        response = requests.post("{}/bulk".format(self.endpoint), data = self.build_request(req_data), headers = self.headers)

        return response

    def __str__(self):
        text = "Transfer of {} {} from {} to {} {}".format(self.amount, self.currency,
                                                        self.source, self.recipient, self.reason)

        return text
    
