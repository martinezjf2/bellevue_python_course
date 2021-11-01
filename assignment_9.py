import requests

key = '6e9453ed5d0d32a75cdda44139ae651d'

def get_weather(name):
    request = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ name + '&appid=' + key)
    validate_request(request) 
    
def user_input():
    city_name = input('Please type in the city: ')
    get_weather(city_name)
    
def display_weather():
    print()
    
def validate_request(request):
    print(request.status_code)
    if (request.status_code == requests.codes.ok):
        promise = request.json()
        retrieve_details(promise)
    else:
        print("Please Provide with a Valid City Name")
        user_input()
    
def retrieve_details(promise):
    main = promise['weather'][0]['main']
    description = promise['weather'][0]['description']
    temperature = promise["main"]["temp"]
    temp_min = promise["main"]["temp_min"]
    temp_max = promise["main"]["temp_max"]
    name = promise['name']
    print("City Name: ", name)
    print("Main: ", main)
    print("Desciption: ", description)
    print("Temperature: ", temperature)
    print("Temp Max ", temp_max)
    print("Temp Min ", temp_min)
    
def kelvin_to_fahrenheit(temp, temp_min, temp_max):
    print()
    
def kelvin_to_celsius(temp, temp_min, temp_max):
    print()
    
def closing_or_choose():
    print()
    
user_input()