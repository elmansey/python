import requests

class ApiClient:

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.weatherapi.com/v1'


    def get_current_temperature(self, city):
        url = f"{self.base_url}/current.json?key={self.api_key}&q={city}"
        response = requests.get(url)
        data = response.json()
        return data['current']['temp_c']


    def get_temperature_after(self, city, days, hour=None):
        url = f"{self.base_url}/forecast.json?key={self.api_key}&q={city}&days={days}"
        response = requests.get(url)
        data = response.json()
        return data['forecast']['forecastday'][0]['day']['avgtemp_c']

    def get_lat_and_long(self, city):
        url = f"{self.base_url}/current.json?key={self.api_key}&q={city}"
        response = requests.get(url)
        data = response.json()
        return (data['location']['lat'], data['location']['lon'])


weather = ApiClient("a34fe1502e46492c80a121339230205")
print(weather.get_current_temperature('London'))
print(weather.get_temperature_after('London', 1))
print(weather.get_lat_and_long('London'))