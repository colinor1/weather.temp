import requests

API_KEY = "" # Paste your API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)


if response.status_code == 200: 
    data = response.json()
    weather = data['weather'][0]['description'].title()
    temperature = round((data["main"]["temp"] - 273.15) * 9/5  + 32, 2)

    print("Weather:", weather)
    print("Temperature:", str(temperature) + "°F")

else:
    print("An erorr occurred.")