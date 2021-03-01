<!--
 * @Author: ruofei
 * @Date: 2021-03-01 14:00:11
 * @LastEditTime: 2021-03-01 18:02:17
 * @LastEditors: Please set LastEditors
 * @Description: ruofei
 * @FilePath: /mugglepay-python-sdk/README.md
-->
# mugglepay-python-sdk
## API request
`pip install -r requirements.txt`
### Athorization
`from mugglepay import MugglepayClient`
`API_KEY = ''  # put your api key here`
`mgp = MugglepayClient(api_key=API_KEY)`

### Create Order
`mgp.create_order(merchat_order_id, price_amount, price_currency, pay_currency, title, description, callback_url, cancel_url, success_url, mobile, fast, token)`

### Get Order
`mgp.get_order(order_id)`

### Get Orders
`mgp.get_orders(status, limit, offset)`

### Checkout Orders
`mgp.checkout_order(status, limit, offset)`

## Run Callback server example
`python callback_server.py`
You need deploy this server online in order to get mugglepay official callback request. Make sure you put correct callback_url when you try to create an order.
