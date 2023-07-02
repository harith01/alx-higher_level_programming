#!/usr/bin/python3
"""POST an email"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]

    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values).encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
