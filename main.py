from crAPIWrapper.crAPIWrapper import crAPIApp

crapi = crAPIApp(domain='localhost',port=8888)

# response = crapi.signup('chuku','chuku@mail.com','1254852','Aa123456')
ok_status,token = crapi.login('bar@mail.com','Aa123456!')

# if ok_status:
#     data = crapi.dashboard(token)

# ok_status, vehicle_data = crapi.get_vehicles(token)

# ok_status,data = crapi.resend_vehicle_email(token)

# ok_status,data = crapi.get_vehicle_location(token,vehicle_data[0]['uuid'])

# status, data =crapi.change_email(token,'bar@mail.com','foo@mail.com')
# status, data = crapi.reset_password(token,'Aa123456!')

# status,data = crapi.get_recent_forum_posts(token)

# print(data)

# status,data = crapi.get_post(token,data[0]['id'])

# print(data)

# status, data = crapi.add_comment_to_post(token,data['id'],'chuku fluku')

# print(data)

# status, data = crapi.send_post(token,'Avada','Kadabra')

# print(data)

# status, data = crapi.get_products(token)

# print(data)

# status, data = crapi.buy_product(token,data['products'][0]['id'],-1)

# print(data)

# status,data = crapi.get_order(token)
# status,data = crapi.get_order(token,3)

# print(data)


# status, data = crapi.validate_coupon(token,'TRAC075')

# status,data = crapi.apply_coupon(token,'TRAC075',42069)

# status,data = crapi.list_emails('bar@mail.com')

# status,data = crapi.get_email(data[0]['ID'])
