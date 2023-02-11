from socket import getaddrinfo
import requests as __requests

def wrapper_post(full_url: str, headers: dict, payload: dict):
    return __requests.post(url=full_url,
                    headers={**headers},
                    json=payload,
                    allow_redirects=True,
                    timeout=10
    )

def is_reachable(domain: str,port: int) -> bool:
    try:
            getaddrinfo(host=domain,port=port)
            return True
    except:
        return False
    

        