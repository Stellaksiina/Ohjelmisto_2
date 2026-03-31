import requests

api_key = "980ac7e6b0472a65a8a59e3a26fb8d55"
city = input("Enter municipality name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]

        print(f"Weather: {description}")
        print(f"Temperature: {temperature} Celsius")
    else:
        print("Error: City not found")
except requests.exceptions.ConnectionError:
    print("Connection Error")