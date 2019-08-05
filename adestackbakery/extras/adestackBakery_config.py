'''
AdestackBakery appsettings file
Contains AdestackBakery_conf class
'''

import os

class AdestackBakery_conf():

    PAYSTACK_URL = 'https://api.paystack.co/'

    PAYSTACK_SECRET_KEY = "sk_test_99d432274bcb2762f94403b0a903145ce5f31476"

    PAYSTACK_PUBLIC_KEY = "pk_test_d23df70a98c6efba7aab7e4b27f3a59fcc48e2da"

    def __new__(cls):
        raise TypeError("Objects can not be created from this class")
