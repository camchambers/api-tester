import requests
import json

class ApiTest:
    path = ''
    expected_status_code = ''

    def __init__(self, expected_status_code, path):
        self.path = path
        self.expected_status_code = expected_status_code

class GetTest(ApiTest):
    def __init__(self, expected_status_code, path):
       super().__init__(expected_status_code, path)

class PostTest(ApiTest):
    data = {}

    def __init__(self, expected_status_code, path, data = {}):
       super().__init__(expected_status_code, path)
       self.data = json.dumps(data)

class ApiTester:
    headers = {}
    api_tests = {}
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
            result = requests.get(url, headers=self.headers)

            if test.expected_status_code == result.status_code:
                print("[PASS]\t\t{}\t\t{}\t\t{}".format(test.expected_status_code, result.status_code, url)) 
            else:
                print("[FAIL]\t\t{}\t\t{}\t\t{}".format(test.expected_status_code, result.status_code, url))

            if self.show_request_responses == True:
                if result.status_code == 200:
                    print("Result:")
                    parsed = json.loads(result.content)
                    print(json.dumps(parsed, indent=4)+ "\n")