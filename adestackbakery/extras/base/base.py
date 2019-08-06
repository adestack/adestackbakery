'''

base.py

'''
import json
from forex_python.converter import CurrencyCodes
from adestackbakery.extras.adestackBakery_config import AdestackBakery_conf

class Base():
    '''

    This is an abstract base class
    
    '''
    PAYSTACK_SECRET_KEY = None
    PAYSTACK_PUBLIC_KEY = None
    PAYSTACK_URL = None

    def __init__(self):

        if type(self) is Base:
            raise TypeError("{} abstract class can not be instantiated".format(Base))

        
        if not AdestackBakery_conf.PAYSTACK_SECRET_KEY or not AdestackBakery_conf.PAYSTACK_PUBLIC_KEY:
            raise ValueError("No secret key or public key found,"
                             "assign values using AdestackBakery_conf.PAYSTACK_SECRET_KEY = SECRET_KEY and"
                             "AdestackBakery_conf.PAYSTACK_PUBLIC_KEY = PUBLIC_KEY")


        self.PAYSTACK_SECRET_KEY = AdestackBakery_conf.PAYSTACK_SECRET_KEY
        self.PAYSTACK_PUBLIC_KEY = AdestackBakery_conf.PAYSTACK_PUBLIC_KEY
        self.PAYSTACK_URL = AdestackBakery_conf.PAYSTACK_URL

    
    def _url(self, endpoint):
        '''
        Method for generating the request url
        Returns a string containing the full request url: paystack api url and the api request endpoint 

        Arguments:
        path(str): A required path argument for the api request endpoint
        '''
        return self.PAYSTACK_URL + endpoint

    def _header(self):
        '''
        Method for generating the request headers.
        Returns a dictionary containing the generated headers

        Arguments :
        '''
        
        headers = {
                'Content-Type':'application/json',
                'Authorization': 'Bearer {}'.format(self.PAYSTACK_SECRET_KEY)
                }

        return headers


    def clean_amount(self, amount):
        '''
        Method to check the validity of the amount arguments. Checks to confirm that amount is an integer
        Return an integer contain a verified amount

        Arguments:
        amount(int): A required amount argument in integer
        '''

        try:
            amount = int(amount)
            
        except ValueError:
            raise ValueError("Invalid amount. Amount(in kobo) should be an integer")

        return amount*100

    def clean_currency(self, currency):

        if not CurrencyCodes().get_symbol(currency.upper()):
            raise ValueError("Invalid currency supplied")

        return currency

    
    def get_request_status(self, data):
        '''
        Method to return the status and message from an API response

        Arguments :
        data : Response as a requests.models.Response
        '''

        return (data.json()["status"])


    def build_request(self, data):
        '''
        Method to build accompaning API request data as JSON
        Return a json object

        Arguments :
        data : Response as a dict
        '''

        if not isinstance(data, dict):
            raise TypeError("Data response argument should be a dictionary")

        return json.dumps(data)

