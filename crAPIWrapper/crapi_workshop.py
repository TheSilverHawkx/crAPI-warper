from crAPIWrapper.wrapper_utils import wrapper_post,wrapper_get

def get_products(base_url: str, headers: dict = {}):
    url_path = '/workshop/api/shop/products'

    function_specific_headers = {
        'Origin': base_url,
        'Referer': '{}/shop'.format(base_url)
    }

    return wrapper_get('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers})

def get_order(base_url: str, order_id: str, headers: dict = {}):
    url_path = '/workshop/api/shop/orders/{}'.format(order_id)

    function_specific_headers = {
        'Origin': base_url,
        'Referer': '{}/shop'.format(base_url)
    }

    return wrapper_get('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers})

def new_order(base_url: str,product_id: int, quantity: int,headers: dict = {}):
    url_path = '/workshop/api/shop/orders'

    function_specific_headers = {
        'Origin': base_url,
        'Referer': '{}/shop'.format(base_url)
    }

    payload = {
        'product_id': product_id,
        'quantity': quantity
    }

    return wrapper_post('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers}, payload)

def return_order(base_url: str,order_id: int, headers: dict = {}):
    url_path = '/workshop/api/shop/orders/return_order?order_id={}'.format(order_id)

    function_specific_headers = {
        'Origin': base_url,
        'Referer': '{}/past-orders'
    }

    payload = {
        'order_id': order_id
    }

    return wrapper_post('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers}, payload)

def get_mechanics( base_url: str, vin: str, headers: dict = {}):
    url_path = '/workshop/api/mechanic'

    function_specific_headers = {
        'Referer': '{}/contact-mechanic?VIN={}'.format(base_url,vin)
    }

    return wrapper_get('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers})

def contact_mechanic(base_url: str, mechanic_code: str, issue_description: str,vin: str, headers: dict = {}):
    url_path = '/workshop/api/merchant/contact_mechanic'

    function_specific_headers = {
        'Origin': base_url,
        'Referer': '{}/contact-mechanic?VIN={}'.format(base_url, vin)
    }

    payload = {
        'mechanic_api': '{}/workshop/api/mechanic/receive_report'.format(base_url),
        'mechanic_code': mechanic_code,
        'number_of_repeats': 1,
        'problem_details': issue_description,
        'repeat_request_if_failed': False,
        'vin': vin
    }

    return wrapper_post('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers}, payload)

def get_mechanic_report(base_url: str, report_id: int, headers: dict = {}):
    url_path = '/workshop/api/mechanic/mechanic_report?report_id={}'.format(report_id)

    return wrapper_get('{}{}'.format(base_url,url_path),headers)
    
def apply_coupon(base_url: str, coupon_code:str, amount: int, headers: dict = {} ):
    url_path = '/workshop/api/shop/apply_coupon'

    function_specific_headers = {
        'Origin': base_url
    }

    payload = {
        'coupon_code': coupon_code,
        'amount': amount
    }

    return wrapper_post('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers}, payload)
