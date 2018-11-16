#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

#====================================================================
choice = input("Please Select one of this choice(1-City. 2-Latitude + Longitude.):")
if choice == '1' :
    city = input('City Name :')
    print(city)
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    url = api_address + city
    json_data = requests.get(url).json()
    print(json_data)
elif choice == '2' :
    lat = input('latitude')
    lon = input('longitude')
    url = 'http://api.openweathermap.org/data/2.5/weather?' +'lat=' + lat + '&lon=' + lon + '&APPID=0c42f7f6b53b244c78a418f4f181282a'
    json_data = requests.get(url).json()
    print(json_data)

