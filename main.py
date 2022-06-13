from scrape import get_weather_data, Print_data

city = input("Enter location:")
data = get_weather_data(city)
Print_data(data)
