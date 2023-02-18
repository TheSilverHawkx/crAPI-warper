
# OWASP crAPI Python Wrapper 

Small wrapper in Python 3 for for OWASP's [crAPI project](https://github.com/OWASP/crAPI).

This module can be used for automating actions for crAPI to test different attacks based on their [official challanges](https://github.com/OWASP/crAPI/blob/develop/docs/challenges.md).

Note: error handling is not finished yet.




## Usage/Examples

There are two ways to this this module.

1. Using the `crAPIApp` class which includes most of the API available via crAPI's postman colleciton and handles passing tokens, generic headers and basic error handling.

```python
from crAPIWrapper.crAPIWrapper import crAPIApp

crapi = crAPIApp(domain='localhost',port=8888)
status,token = crapi.login('bar@mail.com','Aa123456!')

status, products = crapi.get_products(token)

```



2. Using wrappers directly (named structure crapi_*.py and mailhog.py) which don't handle errors.
```python
import crapi_workshop as workshop

headers = {
    'Authorization': 'Bearer ...',
    'content-type': 'application/json'
}

workshop.get_order("https://localhost:8888",2,headers)
```




## Available endpoints
crAPI Community:
* POST /community/api/v2/coupon/validate-coupon
* GET  /community/api/v2/community/posts/recent
* GET  /community/api/v2/community/posts/:id
* GET  /community/api/v2/community/posts/recent
* POST /community/api/v2/community/posts/:id/comment
* POST /community/api/v2/community/posts

crAPI Workshop:
* GET  /workshop/api/shop/products
* GET  /workshop/api/shop/orders/:id
* GET  /workshop/api/shop/orders/all
* POST /workshop/api/shop/orders
* POST /workshop/api/shop/orders/return_order
* GET  /workshop/api/mechanic
* POST /workshop/api/merchant/contact_mechanic
* GET  /workshop/api/mechanic/mechanic_report
* POST /workshop/api/shop/apply_coupon

crAPI Identity:
* POST /identity/api/auth/signup
* POST /identity/api/auth/login
* GET  /identity/api/v2/user/dashboard
* GET  /identity/api/v2/vehicle/vehicles
* POST /identity/api/v2/vehicle/resend_email
* POST /identity/api/v2/vehicle/add_vehicle
* GET  /identity/api/v2/vehicle/:id/location
* POST /identity/api/v2/user/change-email
* POST /identity/api/v2/user/verify-email-token
* POST /identity/api/v2/user/reset-password
* POST /identity/api/auth/forget-password
* POST /identity/api/auth/verify
* POST /identity/api/auth/v3/check-otp

Mailhog:
* GET  /api/v2/search
* GET  /api/v1/messages

## License

[MIT](https://choosealicense.com/licenses/mit/)

