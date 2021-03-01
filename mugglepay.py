'''
Author: ruofei xu
Date: 2021-03-01 14:01:04
LastEditTime: 2021-03-01 16:58:59
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

    # 创建mugglepay订单
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

    # 获取mugglepay订单
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
    
    # 批量获取mugglepay订单
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

    # 结账mugglepay订单
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
        r = requests.get(
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
    # 测试样例
    mgp = MugglepayClient(api_key = '6585f7e0-7a6b-11eb-a075-4d53369a311a')
    print('创建订单测试')
    res = mgp.create_order(
        merchat_order_id='6585f7e0-7a6b-11eb-a075-4d53369a311a',
        price_amount=1,
        price_currency='USD',
        pay_currency='CNY',
        title='Monthly Program x 2',
        description='test python',
        callback_url='https://ecards.com/api/success',
        cancel_url='https://ecards.com/ecardstatus?status=cancel',
        success_url='https://ecards.com/ecardstatus?status=success',
        mobile=False,
        fast=False,
        token='test12345'
    )
    print(res)
    print('获取订单测试')
    print(mgp.get_order(res['order']['order_id']))
    print('批量获取订单接口测试')
    print(mgp.get_orders('NEW', 2, 0))
    print('结账接口测试')
    print(mgp.checkout_order(res['order']['order_id'], 'USD'))
