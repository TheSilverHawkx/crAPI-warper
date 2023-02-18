from crAPIWrapper.wrapper_utils import wrapper_post,wrapper_get

def validate_coupon(base_url: str,coupon_code: str, headers: dict = {}):
    url_path = '/community/api/v2/coupon/validate-coupon'

    function_specific_headers = {
        'Origin': base_url,
        'Referer': '{}/shop'.format(base_url)
    }

    payload = {
        'coupon_code': coupon_code
    }

    return wrapper_post('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers}, payload)

def recent_posts(base_url: str, headers: dict = {}):
    url_path = '/community/api/v2/community/posts/recent'

    function_specific_headers = {
        'Origin': base_url,
        'Referer': '{}/forum'.format(base_url)
    }

    return wrapper_get('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers})

def get_post(base_url: str,post_id: str, headers: dict = {}):
    url_path = '/community/api/v2/community/posts/{}'.format(post_id)

    function_specific_headers = {
        'Referer': '{}/post?post_id={}'.format(base_url,post_id)
    }

    return wrapper_get('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers})

def add_comment(base_url: str,post_id: str,comment: str,headers: dict = {}):
    url_path = '/community/api/v2/community/posts/{}/comment'.format(post_id)

    function_specific_headers = {
        'Origin': base_url,
        'Referer': '{}/post?post_id={}'.format(base_url,post_id)
    }

    payload = {
        'content': comment
    }

    return wrapper_post('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers}, payload)

def add_post(base_url: str,title: str, content: str,headers: dict = {}):
    url_path = '/community/api/v2/community/posts'

    function_specific_headers = {
        'Origin': base_url,
        'Referer': '{}/new-post'
    }

    payload = {
        'title': title,
        'content': content
    }

    return wrapper_post('{}{}'.format(base_url,url_path),{**function_specific_headers,**headers}, payload)