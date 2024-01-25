MY_API = "004fc0e7e8856ccd5cea80f8854fa72a"
import requests


def get_data(place, forecast_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={MY_API}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    num_values = 8*forecast_days
    filtered_data = filtered_data[:num_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
