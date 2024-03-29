import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values).encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        decode_body = body.decode('utf-8')

    print('Your email is:', decode_body)
