

# This week we will work with functions.  For this week’s assignment, write a program that uses a function to convert miles to kilometers.  Your program should prompt the user for the number of miles driven then call a function which converts miles to kilometers.  Check and validate all user input and incorporate Try/Except block(s). The program should then display the total miles and the kilometers.

def main():
    try:
        choice = int(input("\nPlease Choose an option\n\n1. Miles-to-kilometers \n2. Kilometers=to-Miles \n\nEnter a choice : "))
        check_choice(choice)
    except:
        print("Invalid input. Please do not use decimals!")
        main()
    


def Miles_2_kilo(distance):
    return distance / 0.6214


def kilo_2_miles(distance):
    return distance * 0.6214

def check_choice(choice):
    if choice == 1:
            distance_mile = float(input("\nEnter the distance in miles : "))
            mile_to_km = Miles_2_kilo(distance_mile)
            print("\nMiles %.3f mile" %(distance_mile))
            print("\nKilometers %.3f km" %(mile_to_km))
    elif choice == 2:
            distance_km = float(input("\nEnter the distance in kilometers : "))
            km_to_miles = kilo_2_miles(distance_km)
            print("\nKilometers %.3f km" %(distance_km))
            print("\nMiles %.3f mile" %(km_to_miles))
    else:
            print("\nWrong Input Value! Please enter a choice. 1 or 2\n")
            main()        

main()