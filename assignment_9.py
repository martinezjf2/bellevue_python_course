import requests

key = '6e9453ed5d0d32a75cdda44139ae651d'
api_call = 'api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'




def get_weather(name):
    request = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ name + '&appid=' + key)
    validate_request(request)

    
    
def user_input():
    city_name = input('Please type in the city: ')
    get_weather(city_name)
    
def display_weather():
    print()
    
def validate_request(request):
    if (request.status_code == requests.codes.ok):
        promise = request.json()
        retrieve_details(promise)
    else:
        print("Please Provide with a Valid City Name")
        user_input()
    
def retrieve_details(promise):
    main = promise['weather'][0]['main']
    description = promise['weather'][0]['description']
    print("Main: " + main)
    print("Desciption: " + description)
    
    
    
user_input()