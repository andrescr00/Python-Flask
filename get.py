import requests

url = 'http://httpbin.org/get'
args = {'nombre':'andres','apellido':'castano'}
response = requests.get(url, params=args)

if response.status_code == 200 :
	print(response.text) 
