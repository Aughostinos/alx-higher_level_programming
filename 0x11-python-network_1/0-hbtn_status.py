#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    decode_html = html.decode('utf-8')

print('Body response:')
print('\t- type:', type(html))
print('\t- content:', html)
print('\t- utf8 content:', decode_html)
