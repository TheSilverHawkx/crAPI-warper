from wrapper_utils import wrapper_post

def signup(base_url,name,email,number,password,headers: dict = {}):
    url_path = '/identity/api/auth/login'
    
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
    url_path = '/identity/api/auth/signup'

    function_specific_headers = {
        'Origin': base_url,
        'Referer': '{}/login'.format(base_url)
    }

    payload = {
        'email': email,
        'password': password
    }

    return wrapper_post('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers}, payload)