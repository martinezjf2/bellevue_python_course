

# This week we will work with loops. For this week’s assignment, write a program that uses a while loop to determine how long it takes for an investment to double at a given interest rate. The input will be an annualized interest rate and the initial investment amount, and the output is the number of years it takes an investment to double.

initialAmt = 1
rate = float(input('Enter interest rate: '))
finalAmount = initialAmt
years = 0

while finalAmount < 2 * initialAmt:
   years = years + 1
   interest = finalAmount * rate / 100.0
   finalAmount = finalAmount + interest
  

print('At an interest rate of {:.2f}, your initial investment of ${:.2f} will be ${:.2f} in {} years'.format(rate, initialAmt, finalAmount, years))