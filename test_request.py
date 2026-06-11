import requests

url = 'http://localhost:5000/upload'

files = {'shoe_properties': open('uploads/test_3.png', 'rb'),}


print("sending request to flask app...")    

response = requests.post(url, files=files)
print("\n--Response from flask app--")
print(response.text)

