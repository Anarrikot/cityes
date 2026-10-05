import urllib.request
import json

class WeatherData:
    def __init__(self, city, temp, country):
        self.city = city
        self.temp = temp
        self.country = country

    def info(self):
        print(f"{self.country}, {self.city} +{self.temp} °C")


def main():
    cities = []
    with open("vk-task-14.txt", "r") as file:
        for line in file:
            cities.append(line.strip())


    weather_data_list = []
    for city in set(cities):
        with urllib.request.urlopen(f"https://wttr.in/{city}?format=j1")  as response:
            data = json.loads(response.read().decode('utf-8'))
            weather = WeatherData(city, data['current_condition'][0]['temp_C'], data['nearest_area'][0]['country'][0]['value'])
            weather.info()
            weather_data_list.append(weather)

    stats = {}
    for item in weather_data_list:
        if item.country not in stats:
            stats[item.country] = []
        stats[item.country].append(int(item.temp))

    for country, temps in stats.items():
        count = len(temps)
        avg_temp = sum(temps) / count
        min_temp = min(temps)
        max_temp = max(temps)

        print(f"{country} — {count} cities, "
              f"avg: +{avg_temp} °C, "
              f"min: +{min_temp} °C, "
              f"max: +{max_temp} °C")


if __name__ == "__main__":
    main()