import crapi_identity
from json import loads
from wrapper_utils import is_reachable, wrapper_post



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
        self.__base_url = f"{self.__protocol}://{self.__domain}:{self.__port}"

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

            return (False,error_msg_obj['message'])
        else:
            return (True,response.text)
    
