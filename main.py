import api_tester as at

def main():

    host = "http://localhost:54321"

    headers = {
        'content-type': 'application/json',
        'Accept-Charset': 'UTF-8',
        'X-API-Key': "<api-key-here>"
    }

    apiTests = {
        at.GetTest(404,'constituents/000000'),
        at.GetTest(404,'non-existant-path/000000'),
        at.GetTest(200,'constituents/649040'),
        at.GetTest(404,'constituents/profile/000000'),
        at.GetTest(200,'constituents/profile/649040'),
        at.GetTest(404,'constituents/fullprofile/000000'),
        at.GetTest(200,'constituents/fullprofile/417795'),
        at.GetTest(404,'constituents/search/000000'),
        at.GetTest(200,'constituents/search/20242347'),
        at.GetTest(404,'constituents/search/xby2zy94'),
        at.GetTest(200,'constituents/search/jemcclin'),
    }

    apiTester = at.ApiTester(host, apiTests, headers) 
    
    apiTester.run_tests()

if __name__=="__main__":
        main()