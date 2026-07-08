import requests
from datetime import datetime

# Mangalore Coordinates
LATITUDE = 12.9141
LONGITUDE = 74.8560

URL = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={LATITUDE}"
    f"&longitude={LONGITUDE}"
    f"&current=temperature_2m,relative_humidity_2m,pressure_msl,rain"
)

def get_weather():
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()

        current = data["current"]

        weather = {
            "city": "Mangalore",
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "pressure": current["pressure_msl"],
            "rain": current["rain"],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        return weather

    else:
        print("Status Code:", response.status_code)
        print(response.text)
        return None


if __name__ == "__main__":
    weather = get_weather()

    if weather:
        print(weather)