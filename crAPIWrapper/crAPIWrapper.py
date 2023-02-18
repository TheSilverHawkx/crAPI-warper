from json import loads
import crAPIWrapper.crapi_exceptions as crapi_exception
import crAPIWrapper.crapi_identity as crapi_identity
import crAPIWrapper.crapi_workshop as crapi_workshop
import crAPIWrapper.crapi_community as crapi_community
import crAPIWrapper.mailhog as mailhog
from crAPIWrapper.wrapper_utils import is_reachable, wrapper_post



class crAPIApp():

    default_headers = {
        'Accept': "*/*",
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Conneciton': 'keep-alive',
        'Content-Type': 'application/json',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': "?0",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    

    def __init__(self,domain: str, port: int, use_https: bool = False) -> None:
        self.__domain = domain
        self.__port = port
        self.__protocol = "https" if use_https else "http"
        self.__base_url = '{}://{}:{}'.format(self.__protocol,self.__domain,self.__port)
        self.__base_url_mailhog = '{}://{}:{}'.format(self.__protocol,self.__domain,8025)

        if not is_reachable(domain,port):
            print("Unable to connect to crAPI using URL: {}".format(self.__base_url))
            exit(-1)


    def signup(self,name: str, email: str, phone_number: str, password: str,headers: dict = {}) -> tuple:
        
        response = crapi_identity.signup(self.__base_url,
                                         name,
                                         email,
                                         phone_number,
                                         password,
                                         headers={**self.default_headers,**headers})

        if response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            return (False,error_msg_obj['message'])
        else:
            return (True,response.text)

    def login(self, email: str, password: str ,headers:dict = {}) -> tuple:
        response = crapi_identity.login(self.__base_url,
                                         email,
                                         password,
                                         headers={**self.default_headers,**headers})

        if response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            if error_msg_obj['message'] in ('Given Email is not registered! ','Invalid Credentials'):
                raise crapi_exception.InvalidCredentials(email,password,error_msg_obj['message'])
            else:
                return (False,error_msg_obj['message'])
        else:
            return (True,loads(response.text)['token'])
    
    def dashboard(self,token: str, headers: dict = {}) -> tuple:
        auth = {
            'Authorization': 'Bearer {}'.format(token)
        }

        response = crapi_identity.dashboard(self.__base_url,{**auth,**headers})

        if response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            return (False,error_msg_obj['message'])
        else:
            return (True,loads(response.text))
    
    def get_vehicles(self,token:str,headers: dict = {}) -> tuple:
        auth = {
            'Authorization': 'Bearer {}'.format(token)
        }

        response = crapi_identity.vehicles(self.__base_url,{**auth,**headers})

        if response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            return (False,error_msg_obj['message'])
        else:
            return (True,loads(response.text))
    
    def resend_vehicle_email(self,token: str,headers: dict = {}) -> tuple:
        auth = {
            'Authorization': 'Bearer {}'.format(token)
        }

        response = crapi_identity.resend_vehicle_email(self.__base_url,{**auth,**headers})

        if response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            return (False,error_msg_obj['message'])
        else:
            return (True,loads(response.text))

    def get_vehicle_location(self, token: str, vehicle_id: str, headers: dict = {}) -> tuple:
        auth = {
            'Authorization': 'Bearer {}'.format(token)
        }

        response = crapi_identity.get_vehicle_location(self.__base_url,vehicle_id,{**auth,**headers})

        if response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            return (False,error_msg_obj['message'])
        else:
            return (True,loads(response.text))

    def change_email(self,token: str, old_email: str, new_email: str, headers: dict = {}) -> tuple:
        auth = {
            'Authorization': 'Bearer {}'.format(token)
        }

        response = crapi_identity.change_email(self.__base_url,old_email,new_email,{**auth,**headers})

        if response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            return (False,error_msg_obj['message'])
        else:
            return (True,loads(response.text))

    # %?
    def reset_password(self, token: str, new_password: str, headers: dict = {}) -> tuple:
        auth = {
            'Authorization': 'Bearer {}'.format(token)
        }

        response = crapi_identity.reset_password(self.__base_url,new_password,{**auth,**headers})

        if response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            return (False,error_msg_obj['message'])
        else:
            return (True,loads(response.text))

    # %?
    def validate_coupon(self, token: str, coupon_code: str, headers: dict = {}) -> tuple:
        auth = {
            'Authorization': 'Bearer {}'.format(token)
        }

        response = crapi_community.validate_coupon(self.__base_url,coupon_code,{**auth,**headers})

        if response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            return (False,error_msg_obj['message'])
        else:
            return (True,loads(response.text))

    def get_recent_forum_posts(self, token: str, headers: dict = {}) -> tuple:
        auth = {
            'Authorization': 'Bearer {}'.format(token)
        }

        response = crapi_community.recent_posts(self.__base_url,{**auth,**headers})

        if response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            return (False,error_msg_obj['message'])
        else:
            return (True,loads(response.text))

    def get_post(self, token:str, post_id: str, headers: dict = {}) -> tuple:
        auth = {
            'Authorization': 'Bearer {}'.format(token)
        }

        response = crapi_community.get_post(self.__base_url,post_id,{**auth,**headers})

        if response.status_code == 404:
            raise crapi_exception.PostNotFound(post_id,loads(response.text)['message'])

        elif response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            return (False,error_msg_obj['message'])
        else:
            return (True,loads(response.text))

    def add_comment_to_post(self, token: str, post_id: str, content: str, headers: dict = {}) -> tuple:
        auth = {
            'Authorization': 'Bearer {}'.format(token)
        }

        response = crapi_community.add_comment(self.__base_url,post_id, content,{**auth,**headers})

        if response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            return (False,error_msg_obj['message'])
        else:
            return (True,loads(response.text))

    def send_post(self, token: str, title: str, content: str, headers: dict = {}) -> tuple:
        auth = {
            'Authorization': 'Bearer {}'.format(token)
        }

        response = crapi_community.add_post(self.__base_url,title,content,{**auth,**headers})

        if response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            return (False,error_msg_obj['message'])
        else:
            return (True,loads(response.text))
    
    def get_products(self, token: str, headers: dict = {}) -> tuple:
        auth = {
            'Authorization': 'Bearer {}'.format(token)
        }

        response = crapi_workshop.get_products(self.__base_url,{**auth,**headers})

        if response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            return (False,error_msg_obj['message'])
        else:
            return (True,loads(response.text))
    
    def get_order(self, token: str, order_id: str = 'all', headers: dict = {}) -> tuple:
        auth = {
            'Authorization': 'Bearer {}'.format(token)
        }

        response = crapi_workshop.get_order(self.__base_url,order_id,{**auth,**headers})

        if response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            return (False,error_msg_obj['message'])
        else:
            return (True,loads(response.text))
        
    def buy_product(self, token: str, product_id: str, quantity: int, headers: dict = {}) -> tuple:
        auth = {
            'Authorization': 'Bearer {}'.format(token)
        }

        response = crapi_workshop.new_order(self.__base_url,product_id,quantity,{**auth,**headers})

        if response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            return (False,error_msg_obj['message'])
        else:
            return (True,loads(response.text))

    def list_emails(self, email: str, headers: dict = {}) -> tuple:

        response = mailhog.get_emails(self.__base_url_mailhog,email,**headers)

        if response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            return (False,error_msg_obj['message'])
        else:
            return (True,loads(response.text)['items'])
    
    def get_email( self, email_id: str, headers: dict = {}) -> tuple:
        response = mailhog.get_email(self.__base_url_mailhog,email_id,**headers)

        if response.status_code not in range(200,300):
            error_msg_obj = loads(response.text)

            return (False,error_msg_obj['message'])
        else:
            return (True,loads(response.text)['Content']['Body'])

    def apply_coupon(self, token:str, coupon_code: str, amount: int, headers: dict = {}) -> tuple:
        auth = {
            'Authorization': 'Bearer {}'.format(token)
        }

        response = crapi_workshop.apply_coupon(self.__base_url,coupon_code,amount,{**auth,**headers})
        response_text = loads(response.text)

        if response.status_code not in range(200,300):

            return (False,response_text['message'])
        else:
            return (True,response_text['message'])
    
    