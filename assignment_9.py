
# this is the rough draft and will continue to add on some features

import requests
import os
from dotenv import load_dotenv
# https://www.youtube.com/watch?v=YdgIWTYQ69A Hide API Keys in Python using python-dotenvm .env, and gitignore
from termcolor import cprint
# article to fix the import... https://stackoverflow.com/questions/51530437/no-module-named-termcolor/51530570, resolved it by running this command: pip3.9 install termcolor


load_dotenv()
KEY = os.getenv("KEY")

def main():
    welcome()
    user_input()
    print()
    
def welcome():
    cprint("\n-------------------------------------------------", "blue")
    cprint("  Welcome to the Weather App! Let's Get Started  ", 'yellow')
    cprint("-------------------------------------------------\n", 'blue')

# refractor get_weather and user_input functions
def get_weather(name, units):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={name}&appid={KEY}&units={units}"
    request = requests.get(url)
    # https://www.youtube.com/watch?v=lcWfSn6-m_8 video on how to use the requests to retreive data
    validate_request(request, units) 
    
    
def user_input():
    city_name = input('\nPlease type in the city: ')
    if (city_name == 'exit' or city_name == 'Exit' or city_name == 'quit' or city_name == 'Quit' or city_name == 'q' or city_name == 'Q'):
        print("\nThank you! Hope you have a great day!\n")
    else: 
        choose_units(city_name)    
        
        
def choose_units(city_name):       
    choose_unit = input("Type '1' for metric, Type '2' for standard, or Type '3' for imperial: ")
    unit = check_units_of_measure(choose_unit)
    if (unit == False):
        cprint("\nPlease input a Valid Number!", "red")
        choose_units(city_name)
    else:
        get_weather(city_name, unit)
    
def display_weather(name, main, description, temperature, temp_max, temp_min, wind_speed, clouds, humidity, units):
    
    c = display_units_of_measurement_for_wind_speed(units)
    z = display_units_of_measurement(units)
    print('\n-----------------------------------------')
    print("\n  Let's Take A Look at Today's Weather!\n")
    print(f"\nCity Name       :    {name} ")
    print(f"Main            :    {main}")
    print(f"Desciption      :    {description}")
    print(f"Temperature     :    {temperature} {z} ")
    print(f"Temp Max        :    {temp_max} {z} ")
    
    print(f"Wind Speed      :    {wind_speed} {c} ")
    print(f"Clouds          :    {clouds} %")
    print(f"Humidity        :    {humidity} %")
    
    print(f"Temp Min        :    {temp_min} {z} " '\n')
    print('\n-----------------------------------------\n')
    closing_or_choose()
    
def display_units_of_measurement_for_wind_speed(units):
    if (units == 'metric'):
        return 'meter/sec'
    elif (units == 'imperial'):
        return 'miles/hour'
    elif (units == 'standard'):
        return 'meter/sec'
    else:
        return False    
    
def display_units_of_measurement(units):
    if (units == 'metric'):
        return 'degrees Celsius'
    elif (units == 'imperial'):
        return 'degrees Fahrenheit'
    elif (units == 'standard'):
        return 'Kelvin'
    else:
        return False
    

def validate_request(request, units):
    # print(f"Status Code: {request.status_code}")
    if (request.status_code == requests.codes.ok):
        promise = request.json()
        retrieve_details(promise, units)
    else:
        cprint("\nPlease Provide with a Valid City Name: \n", "red")
        user_input()
    
def retrieve_details(promise, units):
    main = promise['weather'][0]['main']
    description = promise['weather'][0]['description']
    temperature = promise["main"]["temp"]
    temp_min = promise["main"]["temp_min"]
    temp_max = promise["main"]["temp_max"]
    name = promise['name']
    wind_speed = promise['wind']['speed']
    clouds = promise['clouds']['all']
    humidity = promise['main']['humidity']
    # icon = promise['weather'][0]['icon']
    # print(icon)
    
    display_weather(name, main, description, temperature, temp_max, temp_min, wind_speed, clouds, humidity, units)
    
def check_units_of_measure(input):
    if (input == '1'):
       return 'metric'
    elif (input == '2'):
       return 'standard'
    elif (input == '3'):
        return 'imperial'
    else:
        return False
        
    
def closing_or_choose():
    choose_input = input("Type '1' to type another city, or Type 'exit' to quit: \n")
    if (choose_input == '1'):
        user_input()
    elif (choose_input == 'exit' or choose_input == 'Exit'):
        cprint("\nThank you! Hope you have a great day!\n", "yellow")
    else:
        cprint("\nPlease type in a valid choice:  \n", "red")
        closing_or_choose()
    
main()