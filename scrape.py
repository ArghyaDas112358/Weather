from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
from googletrans import Translator
import geocoder

translator = Translator()
def scrape_data(session,url):
    html = session.get(url)
    soup = bs(html.text, "html.parser")
    result = {}
    result['region'] = translate2eng(soup.find("div", attrs={"id": "wob_loc"}).text)
    result['temp_now'] = translate2eng(soup.find("span", attrs={"id": "wob_tm"}).text)
    result['dayhour'] = translate2eng(soup.find("div", attrs={"id": "wob_dts"}).text)
    result['weather_now'] = translate2eng(soup.find("span", attrs={"id": "wob_dc"}).text)
    result['precipitation'] = translate2eng(soup.find("span", attrs={"id": "wob_pp"}).text)
    result['humidity'] = translate2eng(soup.find("span", attrs={"id": "wob_hm"}).text)
    result['wind'] = translate2eng(soup.find("span", attrs={"id": "wob_ws"}).text)

    # get next few days' weather
    next_days = []
    days = soup.find("div", attrs={"id": "wob_dp"})
    for day in days.findAll("div", attrs={"class": "wob_df"}):
            day_name = day.findAll("div")[0].attrs['aria-label']
            weather = day.find("img").attrs["alt"]
            temp = day.findAll("span", {"class": "wob_t"})
            max_temp = temp[0].text
            min_temp = temp[2].text
            next_days.append({"name": translate2eng(day_name), "weather": translate2eng(weather), "max_temp": max_temp, "min_temp": min_temp})
    # append to result
    result['next_days'] = next_days
    return result

def get_weather_data(city):
    if city=="":
        City = geocoder.ip('me').city
        print("Current location detected:",City)
        get_weather_data(str(City))
    url = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
    session = HTMLSession()
    try:
        return scrape_data(session,url+str(city))
    except:
        print("wrong address...\nGoing with current location...")
        City = geocoder.ip('me').city
        print(City)
        return get_weather_data(str(City))
def translate2eng(strings):
  return translator.translate(strings).text
def Print_data(data):
    print("Weather for:", data["region"])
    print("Day and time:", data["dayhour"])
    print(f"Temperature now: {data['temp_now']}°C")
    print("Description:", data['weather_now'])
    print("Precipitation:", data["precipitation"])
    print("Humidity:", data["humidity"])
    print("Wind:", data["wind"])
    print("Next days:")
    for dayweather in data["next_days"]:
        print("="*30, dayweather["name"], "="*30)
        print("Description:", dayweather["weather"])
        print(f"Max temperature: {dayweather['max_temp']}°C")
        print(f"Min temperature: {dayweather['min_temp']}°C")


if __name__ == "__main__":
    data = get_weather_data("chuchura")
    Print_data(data)
    