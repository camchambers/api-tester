import requests
import json

class ApiTest:
    path = ''
    expected_status_code = ''

    def __init__(self, expected_status_code, path):
        self.path = path
        self.expected_status_code = expected_status_code

class GetTest(ApiTest):
    request_type='GET '
    def __init__(self, expected_status_code, path):
       super().__init__(expected_status_code, path)

class PostTest(ApiTest):
    request_type='POST'
    data = {}

    def __init__(self, expected_status_code, path, data = {}):
       super().__init__(expected_status_code, path)
       self.data = json.dumps(data)

class ApiTester:
    headers = {}
    api_tests = {}
    show_post_data = False
    show_request_responses = False

    def __init__(self, host, api_tests, headers): 
        self.host = host
        self.api_tests = api_tests
        self.headers = headers

    def run_tests(self):
        print("Running tests...")        
        print("Result\t\tExpected\tActual\t\tEndpoint")

        for test in self.api_tests:
            
            url = self.host + "/" + test.path

            if isinstance(test, GetTest):
                result = requests.get(url, headers=self.headers)
            elif isinstance(test, PostTest):
                result = requests.post(url,headers=self.headers, data=test.data)
                if self.show_post_data == True:
                    post_data = json.loads(test.data)
                    print("POST data:")
                    print(json.dumps(post_data, indent=4)+ "\n")

            if test.expected_status_code == result.status_code:
                print("[PASS]\t\t{}\t\t{}\t\t{}".format(test.expected_status_code, result.status_code, test.request_type + " " + url)) 
            else:
                print("[FAIL]\t\t{}\t\t{}\t\t{}".format(test.expected_status_code, result.status_code, test.request_type + " " + url))

            if isinstance(test, PostTest):
                if self.show_post_data == True:
                    post_data = json.loads(test.data)
                    print("POST data:")
                    print(json.dumps(post_data, indent=4)+ "\n")

            if self.show_request_responses == True:
                if result.status_code == 200:
                    print("Response:")
                    parsed = json.loads(result.content)
                    print(json.dumps(parsed, indent=4)+ "\n")