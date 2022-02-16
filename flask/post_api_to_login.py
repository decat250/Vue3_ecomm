import requests

'''
my_data = {'account': 'abcd', 'password': '1234'}
r = requests.post('http://localhost/api/signin', data = my_data)
print(r.json())
'''

my_data = {'account': 'abcdd', 'password': '1234','email':"asdfg1998",'phone':"1234",'name':"+++"}
r = requests.post('http://localhost/api/signup', data = my_data)
print(r.json())
