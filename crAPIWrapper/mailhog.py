from crAPIWrapper.wrapper_utils import wrapper_post,wrapper_get

def get_emails(base_url: str,email: str, headers: dict = {}):
    url_path = '/api/v2/search?kind=to&query={}&limit=10'.format(email)

    return wrapper_get('{}{}'.format(base_url,url_path),headers)

def get_email(base_url: str, email_id: str, headers: dict = {}):
    url_path = '/api/v1/messages/{}'.format(email_id)

    return wrapper_get('{}{}'.format(base_url,url_path),headers)

