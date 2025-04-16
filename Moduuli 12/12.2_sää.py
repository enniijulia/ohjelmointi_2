import requests

def get_weather(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_description = data["weather"][0]["description"]
        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15

        print(f"Sää: {weather_description.capitalize()}")
        print(f"Lämpötila: {temperature_celsius:.2f} °C")
    else:
        print("Virhe haettaessa säätietoja. Tarkista paikkakunta ja API-avain.")


if __name__ == "__main__":
    city = input("Anna paikkakunnan nimi: ")
    api_key = "d40e23b2411c9888dc64a63524a4a713"
    get_   weather(city, api_key)