# API Tester
> A python script for testing API endpoints

## Example
```python
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
        GetTest('constituens/000000', 404),
        GetTest('constituents/54321', 200),
        GetTest('constituents/profile/000000', 404),
        GetTest('constituents/profile/54321', 200),
        GetTest('constituents/fullprofile/000000', 404),
        GetTest('constituents/fullprofile/54321', 200),
        GetTest('constituents/search/000000', 404),
        GetTest('constituents/search/54321', 200),
        GetTest('constituents/search/zzzzzzzz', 404),
        GetTest('constituents/search/joesmith', 200),
    }

    # Instantiate a tester object and run the tests
    apiTester = ApiTester(host, apiTests, headers) 
    apiTester.run_tests()
```

## Clone
- Clone this repo to your local machine using `git@github.com:camchambers/api-tester.git`

## License
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="https://www.camchambers.com" target="_blank">Cam Chambers</a>.
