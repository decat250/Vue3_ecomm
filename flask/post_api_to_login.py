import requests

'''
my_data = {'account': 'abcd', 'password': '1234'}
r = requests.post('http://localhost/api/signin', data = my_data)
print(r.json())

my_data = {'account': 'abcdd', 'password': '1234','email':"asdfg1998",'phone':"1234",'name':"+++"}
r = requests.post('http://localhost/api/signup', data = my_data)
print(r.json())


my_data = {'account': 'abcd','email':"10966010@ntub.edu.tw"}
r = requests.post('http://localhost/api/resetpwdsendvaild', data = my_data)
print(r.json())
'''


my_data = {'id': '1','code':"2t94y","password":"sdsd123"}
r = requests.post('http://localhost/api/type_get', data = my_data)
print(r.json())