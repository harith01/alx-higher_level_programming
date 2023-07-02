#!/usr/bin/python3
"""
A script that takes in a URL,
sends a request to the URL,
and displays the body of the response,
with error handling
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    try:
        urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
