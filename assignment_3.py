
# Using your flowchart and pseudocode from week 2, write a program that will calculate the cost of installing fiber optic cable at a cost of .87 per ft for a company. Your program should display the company name and the total cost. 

# Steps:
# Display a welcome message for your program. 
# Get the company name from the user
# Get the number of feet of fiber optic to be installed from the user
# Multiply the total cost as the number of feet times .87.
# Display the calculated information and company name.

welcome_message = "\nWelcome\n"
print(welcome_message)
company_name = input("What is your company name?\n").capitalize()
number_in_feet_fiber_optic = input("\nEnter the number of feet of fiber optic\n")
number_in_feet_fiber_optic = float(number_in_feet_fiber_optic)
cost_per_feet = 0.87
total_cost = number_in_feet_fiber_optic * cost_per_feet
final_statement = f"\nThe total cost for {company_name} is {total_cost}\n"
print(final_statement)

# Review
# 10: Created a variable that holds a string of welcome message
# 11: Used the print() function to output my welcome message to welcome my user
# 12: Created company_name variable that will hold the data that the user inputs, and capitalizing the first word of the company, used \n so user can input on a new line
# 13: Created number_in_feet... variable that will hold the data the user inputs for the number of feet of fiber optic, this will be inputed as a string.
# 14: Reassigned the variable declared on line 13, to a conversion from a string to a float
# 15: created a variable that holds the cost per feet as a float
# 16: Created a variable total_cost that holds the result of the cost_per_feet multiplied by the number_in_feet_fiber_optic
# 17: Created a variable that will hold a string including data such as the company_name and the total_cost. Instead of using string concatenation, used string interpolation
# 18: Made sure to use the print function to output and display my final statement to my user

# github repo link: https://github.com/martinezjf2/bellevue_python_course