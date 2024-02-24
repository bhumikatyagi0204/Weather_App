import requests
import json
import win32com.client
def Robo_Speaker(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)
city = input("Enter the name of the city.\n")
url = f"https://api.weatherapi.com/v1/current.json?key=6f1475f366134751844110424242202&q={city}"
r = requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
w = (wdic["current"]["temp_c"])
print(wdic["current"]["temp_c"])
Robo_Speaker(f"The current weather in {city} is {w} degrees")
