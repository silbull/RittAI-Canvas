import requests

def get_weather(location, day="tomorrow"):
    forecast_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{location}.json"
    forecast_req = requests.get(forecast_url)
    return forecast_req