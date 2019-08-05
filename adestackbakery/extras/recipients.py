'''
recipients.py

'''

import requests
from adestackbakery.extras.base.base import Base

class Recipients(Base):

    '''
    Recipients Class
    '''
    
    active = None
    createdAt = None
    updatedAt = None
    currency = None
    email = None
    id = None
    recipient_code = None
    currency = None
    account_number = None
    type = None
    bank_name = None
    bank_code = None
    name = None
    description = None
    is_deleted = None
    recipient_code_or_id = None
    

    def __init__(self):
        super().__init__()

        self.headers = self._header()
        self.endpoint = self._url('transferrecipient')
        
    
    def create_recipient(self, name, account_number, bank_code, description, auth_code="", currency="NGN", type="nuban"):
        
        self.name = name,
        self.account_number = account_number
        self.bank_code = bank_code
        self.auth_code = auth_code
        self.type = type
        self.description = description
        
        self.currency = self.clean_currency(currency)
        
        
        req_data = {
            "name":self.name,
            "account_number":self.account_number,
            "bank_code":self.bank_code,
            "auth_code":self.auth_code,
            "currency":self.currency,
            "type":self.type,
            "description":self.description
            }

        response = requests.post(self.endpoint, data=self.build_request(req_data), headers = self.headers)

        return response
    
        
    def list_recipients(self):
        response = requests.get(self.endpoint, headers = self.headers)
        #recipients = res.json()["data"]

        return response

    def update_recipient(self, recipient_code_or_id, name, email):
        
        self.recipient_code_or_id = recipient_code_or_id
        
        self.name = name
        self.email = email
        
        req_data = {"name": self.name, "email": self.email}
        response = requests.put("{}/{}".format(self.endpoint,self.recipient_code_or_id), data=self.build_request(req_data), headers = self.headers)

        return response

    def delete_recipient(self, recipient_code_or_id):
        
        self.recipient_code_or_id = recipient_code_or_id
        response = requests.delete("{}/{}".format(self.endpoint,self.recipient_code_or_id), headers = self.headers)

        return response
