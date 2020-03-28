import requests
import json

def main():
    host = "http://localhost:54321"

    headers = {
        'content-type': 'application/json',
        'Accept-Charset': 'UTF-8',
        'X-API-Key': "<api key here>"
    }

class ApiTest:
    path = ''
    expected_status_code = ''

    def __init__(self, path, expected_status_code):
        self.path = path
        self.expected_status_code = expected_status_code
