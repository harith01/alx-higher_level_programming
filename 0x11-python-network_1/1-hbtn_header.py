#!/usr/bin/python3
"""Takes a URL, sends a request and displays value of a header variable"""


if __name__ == "__main__":
    import sys
    import urllib.request

    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as res:
        print(res.headers.get('X-Request-Id'))
