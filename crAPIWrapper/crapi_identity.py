from crAPIWrapper.wrapper_utils import wrapper_post,wrapper_get

def signup(base_url,name,email,number,password,headers: dict = {}):
    url_path = '/identity/api/auth/signup'
    
    function_specific_headers = {
        'Origin': base_url,
        'Referer': '{}/login'.format(base_url)
    }

    payload = {
        'name': name,
        'email': email,
        'number': number,
        'password': password
    }

    return wrapper_post('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers}, payload)
        
def login(base_url,email,password, headers: dict = {}):
    url_path = '/identity/api/auth/login'

    function_specific_headers = {
        'Origin': base_url,
        'Referer': '{}/login'.format(base_url)
    }

    payload = {
        'email': email,
        'password': password
    }

    return wrapper_post('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers}, payload)

def dashboard(base_url,headers:dict = {}):
    url_path = '/identity/api/v2/user/dashboard'

    function_specific_headers = {
        'Referer': '{}/login'.format(base_url)
    }

    return wrapper_get('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers})

def vehicles(base_url: str, headers:dict = {}):
    url_path = '/identity/api/v2/vehicle/vehicles'

    function_specific_headers = {
        'Referer': '{}/dashboard'.format(base_url)
    }

    return wrapper_get('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers})

def resend_vehicle_email(base_url: str, headers:dict = {}):
    url_path = '/identity/api/v2/vehicle/resend_email'

    function_specific_headers = {
        'Origin': base_url,
        'Referer': '{}/dashboard'.format(base_url)
    }

    return wrapper_post('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers},{})

def add_vehicle(base_url: str, pin: int, vin: str, headers:dict = {}):
    url_path = '/identity/api/v2/vehicle/add_vehicle'

    function_specific_headers = {
        'Origin': base_url,
        'Referer': '{}/verify-vehicle'.format(base_url)
    }

    payload = {
        'vin': vin,
        'pincode': pin
    }

    return wrapper_post('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers}, payload)

def get_vehicle_location(base_url: str, vehicle_id: str, headers: dict = {}):
    url_path = '/identity/api/v2/vehicle/{}/location'.format(vehicle_id)

    function_specific_headers = {
        'Referer': '{}/dashboard'.format(base_url)
    }

    return wrapper_get('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers})

def change_email(base_url: str,old_email: str, new_email: str,headers: dict = {}):
    url_path = '/identity/api/v2/user/change-email'

    function_specific_headers = {
        'Origin': base_url,
        'Referer': '{}/change-email'.format(base_url)
    }

    payload = {
        'new_email': new_email,
        'old_email': old_email
    }

    return wrapper_post('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers}, payload)

def verify_email_token(base_url: str,new_email: str, email_token: str,headers: dict = {}):
    url_path = '/identity/api/v2/user/verify-email-token'

    function_specific_headers = {
        'Origin': base_url,
        'Referer': '{}/change-email'.format(base_url)
    }

    payload = {
        'new_email': new_email,
        'token': email_token
    }

    return wrapper_post('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers}, payload)

def reset_password(base_url: str, new_password: str, headers: dict = {}):
    url_path = '/identity/api/v2/user/reset-password'

    function_specific_headers = {
        'Origin': base_url,
        'Referer': '{}/reset-password'.format(base_url)
    }

    payload = {
        'password': new_password
    }

    return wrapper_post('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers}, payload)

def forgot_password(base_url: str, email: str, headers: dict = {}):
    url_path = '/identity/api/auth/forget-password'

    payload = {
        'email': email
    }

    return wrapper_post('{}{}'.format(base_url,url_path),headers, payload)

def verify_token(base_url: str, token: str, headers: dict = {}) -> tuple:
    url_path = '/identity/api/auth/verify'

    payload = {
        'token': token
    }

    return wrapper_post('{}{}'.format(base_url,url_path),headers, payload)

def check_opt(base_url: str, email:str, password:str , otp:str, headers: dict = {}) -> tuple:
    url_path = '/identity/api/auth/v3/check-otp'

    payload = {
        'email': email,
        'otp': otp,
        'password': password
    }

    return wrapper_post('{}{}'.format(base_url,url_path),headers, payload)

