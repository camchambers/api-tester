import requests

host = "https://<hostname>/"

headers = {
    'content-type': 'application/json',
    'Accept-Charset': 'UTF-8',
    'x-api-key': "<api key>"
}

endpoints = {
    {'method': 'get', 'path': 'constituents/profile/000000'},
    {'method': 'get', 'path': 'constituents/profile/100000'},
    {'method': 'get', 'path': 'constituents/profile/abcdef'}
}

def test_endpoint(host, endpoint, headers, method="get", data=''):
    print("Testing endpoint " + endpoint)
    url = host + endpoint
    payload = open("request.json")
    results = requests.get(url, data=payload, headers=headers)
    print(results.content)