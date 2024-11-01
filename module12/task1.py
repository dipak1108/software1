import requests


def fetch_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()
        print(joke_data['value'])
    else:
        print("Failed to retrieve joke.")


fetch_chuck_norris_joke()
