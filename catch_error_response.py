import requests

# Make API call which returns response with exception
URL = 'htttttps://app.github.com/'
try:
    response = requests.get(URL)
except Exception as e:
    print(e)
