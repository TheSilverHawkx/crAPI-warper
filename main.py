from crAPIWarper.crAPIWarper import crAPIApp

crapi = crAPIApp(domain='localhost',port=8888)

response = crapi.signup('chuku','chuku@mail.com','1254852','Aa123456')
response = crapi.login('foo@mail.com','Aa123456!')

print(response)