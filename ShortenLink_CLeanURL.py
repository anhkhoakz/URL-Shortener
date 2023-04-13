import requests

session = requests.Session()
session.headers.update({'Content-Type': 'application/json'})


def shorten_url(url):
    endpoint = 'https://cleanuri.com/api/v1/shorten'
    payload = {'url': url}
    try:
        response = session.post(endpoint, json=payload)
        response.raise_for_status()
        result = response.json()
        return result['result_url']
    except requests.exceptions.RequestException:
        return None


def main():
    print("SHORTEN URL")
    while True:
        long_url = input("Enter a link: ")
        short_url = shorten_url(long_url)
        print(short_url)


if __name__ == "__main__":
    main()
