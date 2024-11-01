import requests


def get_weather(municipality, api_key):

    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "485e52c34109b95876954c9316a77af9"

   # request ="https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"


    # Parameters for the request, including the municipality name and API key
    params = {
        "q": municipality,
        "appid": api_key
    }


    response = requests.get(url, params=params)

    if response.status_code == 200:
        weather_data = response.json()

        weather_description = weather_data['weather'][0]['description']
        temperature_kelvin = weather_data['main']['temp']

        temperature_celsius = temperature_kelvin - 273.15

        print(f"Weather: {weather_description.capitalize()}")
        print(f"Temperature: {temperature_celsius:.2f}°C")
    else:
        print("Failed to retrieve weather data. Please check the municipality name or API key.")



if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    municipality = input("Enter the name of a municipality: ")

    get_weather(municipality, api_key)
