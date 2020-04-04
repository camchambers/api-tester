# API Tester
> A python script for testing API endpoints

## Example
```python

import api_tester as at

def main():

    # Specify the host you wish to test
    host = "http://localhost:54321"

    # Specify headers that will be attached to requests
    headers = {
        'content-type': 'application/json',
        'Accept-Charset': 'UTF-8',
        'X-API-Key': "<api key here>"
    }

    # Define all of the tests to run (either a GET or POST test)
    # and the expected HTTP status code returned by each test
    apiTests = {
        at.GetTest('constituents/000000', 404),
        at.GetTest('constituents/54321', 200),
        at.GetTest('constituents/profile/000000', 404),
        at.GetTest('constituents/profile/54321', 200),
        at.GetTest('constituents/fullprofile/000000', 404),
        at.GetTest('constituents/fullprofile/54321', 200),
        at.GetTest('constituents/search/000000', 404),
        at.GetTest('constituents/search/54321', 200),
        at.GetTest('constituents/search/zzzzzzzz', 404),
        at.GetTest('constituents/search/joesmith', 200),
    }

    # Instantiate a tester object and run the tests
    apiTester = ApiTester(host, apiTests, headers) 
    apiTester.run_tests()
   
if __name__=="__main__":
        main()
    
```

## Clone
- Clone this repo to your local machine using `git@github.com:camchambers/api-tester.git`

## License
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="https://www.camchambers.com" target="_blank">Cam Chambers</a>.
