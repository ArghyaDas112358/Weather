# Weather
A simple python app for getting weather information based on geolocation.

## Installation
```
git clone https://github.com/ArghyaDas112358/Weather.git
cd Weather
pip install requirement.txt
```
If this does not work, then maybe python2 is installed in the system or none. Try installing with oython3 3 and use ```pip3``` instead of ```pip```.
# How to use
The app is straightforward to use. Just run the ```main.py``` file, and you are good to go. If you know your current location, then you may enter it. If you don't know your current location, don't worry, the program will auto-detect the current geolocation and display the weather information for it.
### If location is known
```
python3 main.py
Enter location:kolkata
Weather for: Kolkata, West Bengal
Day and time: Tuesday, 12:00 am
Temperature now: 30°C
Description: Mostly cloudy
Precipitation: 3%
Humidity: 84%
Wind: 8 km / h
Next days:
============================== Tuesday ==============================
Description: Mostly cloudy
Max temperature: 36°C
Min temperature: 29°C
============================== Wednesday ==============================
Description: Isolated thunderstorms
Max temperature: 34°C
Min temperature: 29°C 
```
### If location is not known
```
Enter location:
Current location detected: Kolkata
Weather for: Kolkata, ######
Day and time: Tuesday, 12:00 am
Temperature now: 30°C
Description: Mostly cloudy
Precipitation: 3%
Humidity: 85%
Wind: 8 km / h
Next days:
============================== Tuesday ==============================
Description: Mostly cloudy
Max temperature: 36°C
Min temperature: 29°C
============================== Wednesday ==============================
Description: Isolated thunderstorms
Max temperature: 33°C
Min temperature: 29°C
```
