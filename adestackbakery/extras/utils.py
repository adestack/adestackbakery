'''
utils.py
'''
import requests
from adestackbakery.extras.base.base import Base

# base.base import Base


class Utils(Base):
    def __init__(self):
        super().__init__()

        self.headers = self._header()
        self.endpoint = self._url('bank')

    
    def fetch_banks(self):
        '''
        Method to retrieve bank name and bank code from an API

        Arguments :
        
        '''

        response = requests.get(self.endpoint, headers = self.headers)

        return response

    def balance_enquiry(self):
        '''
        Method to retrieve balance from Paystack account

        Arguments :
        
        '''
        
        self.endpoint = self._url('balance')

        response = requests.get(self.endpoint, headers = self.headers)

        return response
        
    def verify_account_number(self, account_number, bank_code):
        
        self.account_number = account_number
        self.bank_code = bank_code

        req_data = {
                "account_number": account_number,
                "bank_code": bank_code,
            }
        print(req_data)
        response = requests.get("https://api.paystack.co/bank/resolve", data = self.build_request(req_data), headers = self.headers)
        #response = requests.get("{}/resolve".format(self.endpoint), data = self.build_request(req_data), headers = self.headers)
        print(response)
        return response
