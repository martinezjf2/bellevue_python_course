


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
number_in_feet_fiber_optic = float(input("\nEnter the number of feet of fiber optic\n"))
# print(number_in_feet_fiber_optic)

# Modify your week 3 program so that if the user purchases more than 100 feet they are charged $.80 per foot.  If the user purchases more than 250 feet they will be charged $.70 per foot.  If they purchase more than 500 feet they will be charged $.50 per foot.

if number_in_feet_fiber_optic > 100 and number_in_feet_fiber_optic <= 250:
    cost_per_feet = 0.80
elif number_in_feet_fiber_optic > 250 and number_in_feet_fiber_optic <= 500:
    cost_per_feet = 0.70
elif number_in_feet_fiber_optic > 500:
    cost_per_feet = .50
else:
    cost_per_feet = .87

total_cost = number_in_feet_fiber_optic * cost_per_feet


final_statement = f"\nThe total cost for {company_name} for {number_in_feet_fiber_optic} feet is ${total_cost}\n"
print(final_statement)

# Review
# 10: Created a variable that holds a string of welcome message
# 11: Used the print() function to output my welcome message to welcome my user
# 12: Created company_name variable that will hold the data that the user inputs, and capitalizing the first word of the company, used \n so user can input on a new line
# 13: Created number_in_feet... variable that will hold the data the user inputs for the number of feet of fiber optic, this will be inputed as a string, refractored from assignment 3.1, converted the string to a float in one same line here
# 14: Prints number_in_feet.. debugging to see if it is a float, commented out...

# Conditionals using if/elif/else statements

# 18-19: Check that if conditional was greater than 100 and if number_of_feet was less than or equal to 250, then declare and assign cost_per_feet to be .80
# 20-21: Used elif if first conditional evaluates to false, checked number_of_feet was greater than 250 and if number_of_feet was less than or equal to 500, assign cost_per_feet to be .70
# 22-23: Used elif if first and second conditions evaluates to false, checked number_of_feet was greater than 500, if it evaluates to true, assign cost_per_feet to be .50
# 24-25: Used an else statement to assign cost_per_feet to be .87 if all conditions above evaluate to false.


# 28: Created a variable total_cost that holds the result of the cost_per_feet multiplied by the number_in_feet_fiber_optic
# 29: Created a variable that will hold a string including data such as the company_name and the total_cost. Instead of using string concatenation, used string interpolation
# 30: Made sure to use the print function to output and display my final statement to my user





