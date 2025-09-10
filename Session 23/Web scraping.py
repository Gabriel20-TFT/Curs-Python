import requests

if __name__ == '__main__':
    # response = requests.get('https://httpbin.org/basic-auth/user/pass')
    response = requests.get('https://www.google.com')
    print(response.status_code)
    print(response.text)
    # print(response.json())
    print(response.headers)
