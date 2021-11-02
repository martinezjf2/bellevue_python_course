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
    # type_zip_or_city_name()
    # delete the user_input() call on line 16
    user_input()
    print()
    
def welcome():
    cprint("\n-------------------------------------------------", "blue")
    cprint("  Welcome to the Weather App! Let's Get Started  ", 'yellow')
    cprint("-------------------------------------------------\n", 'blue')


def get_weather(name, units):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={name}&appid={KEY}&units={units}"
    request = requests.get(url)
    # https://www.youtube.com/watch?v=lcWfSn6-m_8 video on how to use the requests to retreive data
    validate_request(request, units) 
    
    
def user_input():
    city_name = input('Please type in the city: ')
    if (city_name == 'exit' or city_name == 'Exit' or city_name == 'quit' or city_name == 'Quit' or city_name == 'q' or city_name == 'Q'):
        print("\nThank you! Hope you have a great day!\n")
    choose_units(city_name)    
        
        
def choose_units(city_name):       
    choose_unit = input("Type '1' for metric, Type '2' for standard, or Type '3' for imperial: ")
    unit = check_units_of_measure(choose_unit)
    get_weather(city_name, unit)
    
    
def display_weather(name, main, description, temperature, temp_max, temp_min, units):
    print(units)
    print("\nCity Name: ", name)
    print("Main: ", main)
    print("Desciption: ", description)
    print("Temperature: ", temperature)
    print("Temp Max ", temp_max)
    print("Temp Min ", temp_min, '\n')
    closing_or_choose()
    
def validate_request(request, units):
    # print(f"Status Code: {request.status_code}")
    if (request.status_code == requests.codes.ok):
        promise = request.json()
        retrieve_details(promise, units)
    else:
        print("Please Provide with a Valid City Name: \n")
        user_input()
    
def retrieve_details(promise, units):
    main = promise['weather'][0]['main']
    description = promise['weather'][0]['description']
    temperature = promise["main"]["temp"]
    temp_min = promise["main"]["temp_min"]
    temp_max = promise["main"]["temp_max"]
    name = promise['name']
    display_weather(name, main, description, temperature, temp_max, temp_min, units)
    
def kelvin_to_fahrenheit(temp, temp_min, temp_max):
    print()
    
def kelvin_to_celsius(temp, temp_min, temp_max):
    print()
    
# def type_zip_or_city_name():
#     city_or_zip = input("Type '1' to input zip OR type '2' to input city name")
#     if (city_or_zip == '1'):
#         zipcode = input("Please enter a zipcode: ")
#         get_weather_by_zip(zipcode)
#     elif (city_or_zip == '2'):
#         user_input()
    
def check_units_of_measure(input):
    print(input)
    if (input == '1'):
       return 'metric'
    elif (input == '2'):
       return 'standard'
    elif (input == '3'):
        return 'imperial'
    else:
        print("Please type in a valid number!")
        choose_units()
        

    
def closing_or_choose():
    choose_input = input("Type '1' to type another city, or Type 'exit' to quit: \n")
    if (choose_input == '1'):
        user_input()
    elif (choose_input == 'exit' or choose_input == 'Exit'):
        print("\nThank you! Hope you have a great day!\n")
    else:
        print("\nPlease type in a valid choice:  \n")
        closing_or_choose()
    
main()