import requests
import json

def main():
    host = "http://localhost:54321"

    headers = {
        'content-type': 'application/json',
        'Accept-Charset': 'UTF-8',
        'x-api-key': "<api key here>"
    }

    endpoints = [
        {'method': 'get', 'path': 'constituents/649040'},
        {'method': 'get', 'path': 'constituents/profile/649040'},
        {'method': 'get', 'path': 'constituents/profile/000000'},
        {'method': 'get', 'path': 'constituents/profile/649040'},
    ]      

    for endpoint in endpoints:
        test_endpoint(host, endpoint['path'], headers, endpoint['method'])

def test_endpoint(host, endpoint, headers, method="get", data=''):
    print("Testing endpoint \"" + endpoint + "\"")
    url = host + "/" + endpoint
    result = requests.get(url, headers=headers)

    if result.status_code != 200:
        print("Request failed with response {}\n".format(result.status_code)) 
        return

    print("Result:")
    parsed = json.loads(result.content)
    print(json.dumps(parsed, indent=4)+ "\n")

if __name__=="__main__":
        main()
