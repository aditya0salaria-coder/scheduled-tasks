import requests
import os

api_key = os.environ.get("OWM_api_key")

if not api_key:
    raise SystemExit("OWM_api_key is not set")
    
Own_EndPoint = "http://api.openweathermap.org/data/2.5/forecast"

# print("Key loaded:", api_key is not None)
# print("Key length:", len(api_key) if api_key else 0)

parameter = {
    "lat" : 32.259541,
    "lon" : 75.632072,
    "appid": api_key,
    "cnt" : 4,
}

response = requests.get(Own_EndPoint, params=parameter)

# response = requests.get(url=f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid={api_key}")
# print(response.status_code)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

print(weather_data["list"][0]["weather"][0]["id"])

rain_found = False
for item in weather_data["list"]:
    if item["weather"][0]["id"] <700:
        rain_found = True
if rain_found:
    print("Bring Umbrella")
else:
    print("No rain")

# for  in weather_data["list"]:
#     print(item["w"])
