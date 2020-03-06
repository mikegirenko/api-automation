import requests

# Make API call and save response
URL = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(URL)

print('Status code:', response.status_code)
print('Json', response.json())
print('Text', response.text)
print('Total repositories:', response.json()['total_count'])
