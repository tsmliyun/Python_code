import requests

# url = 'http://httpbin.org/get'
# data = {'key': 'value', 'abc': 'xyz'}
# response = requests.get(url, data)
# print(response.text)


url = 'http://httpbin.org/post'
data = {'key': 'value', 'abc': 'xyz'}
response = requests.post(url, data)
print(response.json())