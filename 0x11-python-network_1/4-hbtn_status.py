#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


import requests


url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url)
html = response.text

print('Body response:')
print('\t- type:', type(html))
print('\t- content:', html)
