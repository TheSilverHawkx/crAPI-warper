from socket import getaddrinfo
import requests as __requests

REQUEST_TIMEOUT = 10

def is_reachable(domain: str,port: int) -> bool:
    try:
            getaddrinfo(host=domain,port=port)
            return True
    except:
        return False

def wrapper_post(full_url: str, headers: dict, payload: dict):
    return __requests.post(url=full_url,
                    headers={**headers},
                    json=payload,
                    allow_redirects=True,
                    timeout=REQUEST_TIMEOUT
    )

    
def wrapper_get(full_url: str,headers: dict):
    return __requests.get(url= full_url,
                          headers={**headers},
                          allow_redirects=True,
                          timeout=REQUEST_TIMEOUT)