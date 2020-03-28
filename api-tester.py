import requests
import json

def main():
    host = "http://localhost:54321"

    headers = {
        'content-type': 'application/json',
        'Accept-Charset': 'UTF-8',
        'X-API-Key': "<api key here>"
    }

    apiTests = {
        GetTest('constituens/000000', 404),
        GetTest('constituents/649040', 200),
        GetTest('constituents/profile/000000', 404),
        GetTest('constituents/profile/649040', 200),
        GetTest('constituents/fullprofile/000000', 404),
        GetTest('constituents/fullprofile/417795', 200),
        GetTest('constituents/search/000000', 404),
        GetTest('constituents/search/20242347', 200),
        GetTest('constituents/search/xby2zy94', 404),
        GetTest('constituents/search/jemcclin', 200),
    }

    apiTester = ApiTester(host, apiTests, headers) 
    apiTester.run_tests()

class ApiTest:
    path = ''
    expected_status_code = ''

    def __init__(self, path, expected_status_code):
        self.path = path
        self.expected_status_code = expected_status_code

class GetTest(ApiTest):
    def __init__(self, path, expected_status_code):
       super().__init__(path, expected_status_code)

class PostTest(ApiTest):
    data = {}

    def __init__(self, path, expected_status_code, data = {}):
       super().__init__(path, expected_status_code)
       self.data = data

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

if __name__=="__main__":
        main()