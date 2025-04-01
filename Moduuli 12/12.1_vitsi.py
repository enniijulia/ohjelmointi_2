import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        vitsi = response.json().get("value")
        print(vitsi)
    else:
        print("Virhe haettaessa vitsiä")

if __name__ == "__main__":
    get_chuck_norris_joke()
