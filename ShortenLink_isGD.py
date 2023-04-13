import requests

# Create a session object to reuse for all requests
session = requests.Session()


def shorten_url(url):
    api_url = f"http://is.gd/create.php?format=simple&url={url}"
    response = session.get(api_url)
    if response.status_code == 200:
        return response.text
    else:
        return None


# Cache for frequently accessed URLs
url_cache = {}


def lookup_url(shorturl, format='simple', callback=None):
    if shorturl in url_cache:
        return url_cache[shorturl]

    url = 'https://is.gd/forward.php'
    params = {'shorturl': shorturl, 'format': format, 'callback': callback}
    response = session.get(url, params=params)

    if response.status_code == 200:
        if format == 'simple':
            long_url = response.text.strip()
        elif format == 'json':
            data = response.json()
            if callback:
                long_url = f"{callback}({data});"
            else:
                long_url = data
        elif format == 'xml':
            long_url = response.text.strip()
        else:
            long_url = response.text.strip()

        # Add the URL to the cache
        url_cache[shorturl] = long_url
        return long_url
    else:
        return None


def menu():
    while True:
        print("Please choose an option")
        print("1. Shorten a URL")
        print("2. Lookup a shortened URL")
        choice = input("Enter a choice: ")
        if choice == '1':
            url = input("Enter the URL to shorten: ")
            short_url = shorten_url(url)
            if short_url:
                print(f"Shortened URL: {short_url}")
            else:
                print("Failed to shorten URL.")
        elif choice == '2':
            url = input("Enter the shortened URL to lookup: ")
            long_url = lookup_url(url)
            if long_url:
                print(f"Original URL: {long_url}")
            else:
                print("Failed to lookup shortened URL.")
        else:
            print("Invalid choice. Please enter either '1' or '2'.")


def main():
    menu()


if __name__ == "__main__":
    main()
