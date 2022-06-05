import requests

API_KEY = "yourapikey"

BASE_URL = f"https://api.openweathermap.org/data/2.5/weather"

city = str(input("[+] City: "))

REQUEST_URL = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(REQUEST_URL)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print(f"[+] Dumped the weather data for {city}\n")
    print(f"Weather: {weather}")
    print(f"Temperature: {temperature}")
else:
    print("[-] An error in fetching the data")

