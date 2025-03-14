import requests

# OpenWeather API Key
API_KEY = '30d4741c779ba94c470ca1f63045390a'

def get_weather(city):
    """Fetch and display weather information for a given city."""
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={API_KEY}"
        response = requests.get(url)
        data = response.json()

        if data['cod'] == '404':
            print("No city found. Please enter a valid city name.")
        else:
            city_name = data.get('name', 'Unknown Location')
            weather = data['weather'][0]['description'].capitalize()
            temp = round(data['main']['temp'])
            humidity = data['main']['humidity']

            print("\nWeather Report:")
            print(f"{'City:':<12} {city_name}")
            print(f"{'Temperature:':<12} {temp}ºF")
            print(f"{'Humidity:':<12} {humidity}%")
            print(f"{'Condition:':<12} {weather}")

    except requests.exceptions.RequestException as e:
        print("Error: Unable to fetch weather data. Please check your connection.")
        print(e)

if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    if city:
        get_weather(city)
    else:
        print("Error: No city entered. Please enter a valid city name.")