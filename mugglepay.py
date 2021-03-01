'''
Author: ruofei xu
Date: 2021-03-01 14:01:04
LastEditTime: 2021-03-01 17:47:39
LastEditors: Please set LastEditors
Description: mugglepay sdk for payment
FilePath: /mugglepay-python-sdk/mugglepay.py
'''

import requests


class MugglepayClient:
    def __init__(
            self,
            api_key: str,
		    api_url: str = "https://api.mugglepay.com/v1",
        ):
            if api_key == "":
                raise ValueError('application key is not valid')
            self.api_key = api_key
            self.api_url = api_url

    # create mugglepay order
    def create_order(
        self,
        merchat_order_id: str,
        price_amount: float,
        price_currency: str,
        pay_currency: str,
        title: str,
        description: str,
        callback_url: str,
        cancel_url: str,
        success_url: str,
        mobile: bool,
        fast: bool,
        token: str
    ):
        if merchat_order_id == "":
            raise ValueError('merchant order id is not valid')
        url = '{}/orders'.format(self.api_url)
        headers = {'Content-Type': 'application/json', 'token': self.api_key}
        data = {
                "merchat_order_id": merchat_order_id,
                "price_amount": price_amount,
                "price_currency": price_currency,
                "pay_currency": pay_currency,
                "title": title,
                "description": description,
                "callback_url": callback_url,
                "cancel_url": cancel_url,
                "success_url": success_url,
                "mobile": mobile,
                "fast": fast,
                "token": token
        }
        r = requests.post(
            url = url,
            headers = headers,
            json = data
        )
        
        try:
            return r.json()
        except Exception:
            return {
                'status': r.status_code
            }

    # get mugglepay order
    def get_order(
        self,
        order_id: str
    ):
        if order_id == "":
            raise ValueError('order id is not valid')

        url = '{}/orders/{}'.format(self.api_url, order_id)
        headers = {'Content-Type': 'application/json', 'token': self.api_key}
        data = {
            "order_id": order_id
        }
        r = requests.get(
            url=url,
            headers=headers
        )
        
        try:
            return r.json()
        except Exception:
            return {
                'status': r.status_code
            }
    
    # get mugglepay orders
    def get_orders(
        self,
        status: str = None,
        limit: int = 10,
        offset: int = 0,
    ):
        url = '{}/orders'.format(self.api_url)
        headers = {'Content-Type': 'application/json', 'token': self.api_key}
        params = {
            "status": status,
            "limit": limit,
            "offset": offset
        }
        r = requests.get(
            url=url,
            headers=headers,
            params=params
        )
        
        try:
            return r.json()
        except Exception:
            return {
                'status': r.status_code
            }

    # checkout mugglepay order
    def checkout_order(
        self,
        order_id: str,
        pay_currency: str,
    ):
        if order_id == "":
            raise ValueError('order id is not valid')

        url = '{}/orders/{}/checkout'.format(self.api_url, order_id)
        headers = {'Content-Type': 'application/json', 'token': self.api_key}
        data = {
            "order_id": order_id,
            "pay_currency": pay_currency
        }
        r = requests.post(
            url = url,
            headers = headers,
            json = data
        )
        
        try:
            return r.json()
        except Exception:
            return {
                'status': r.status_code
            }

if __name__ == "__main__":
    # test case
    API_KEY = ''  # put your api key
    mgp = MugglepayClient(api_key=API_KEY)
    print('create order test')
    res = mgp.create_order(
        merchat_order_id='your_order_id',
        price_amount=1,
        price_currency='USD',
        pay_currency='CNY',
        title='Monthly Program x 2',
        description='test python',
        callback_url='https://mugglepay_callback_api',
        cancel_url='https://mugglepay?status=cancel',
        success_url='https://mugglepay?status=success',
        mobile=False,
        fast=False,
        token='test12345'
    )
    print(res)
    print('get order test')
    print(mgp.get_order(res['order']['order_id']))
    print('get orders test')
    print(mgp.get_orders('NEW', 2, 0))
    print('checkout order test')
    print(mgp.checkout_order(res['order']['order_id'], 'EOS'))
