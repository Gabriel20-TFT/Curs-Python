import requests

if __name__ == '__main__':
    # response = requests.get('https://httpbin.org/basic-auth/user/pass')
    response = requests.post('https://httpbin.org/status/404')
    print(response.status_code)
    print(response.text)
    # print(response.json())
    print(response.headers)
