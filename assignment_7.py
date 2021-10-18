
# This week we will work with dictionaries.  Create a program that includes a dictionary of stocks. Your dictionary should include at least 10 ticker symbols.  The key should be the stock ticker symbol and the value should be the current price of the stock (the values can be fictional).  Ask the user to enter a ticker symbol.  Your program will search the dictionary for the ticker symbol and then print the ticker symbol and the stock price.  If the ticker symbol isn’t located print a message indicating that the ticker symbol wasn’t found.


stocks = { "AAPL" : 144.84, "TMUS" : 117.56, "GOOGL" : 2827.36, "AMZN" : 3409.02, "TSLA" : 843.03 , \
           "DIS" : 176.46, "NASDAQ" : 14897.34, "YUM" : 125.21, "FB" : 324.76 , "NFLX" : 628.29}
          
ticker = input('Enter a ticker symbol (e.g. GOOGL). Type QUIT to stop: ')
while not ticker == "QUIT":
   if ticker in stocks:
       print('{} : {}'.format(ticker, stocks[ticker]))
   else:
       print('{} not found'.format(ticker))

   ticker = input('Enter a ticker symbol (e.g. GOOGL). Type QUIT to stop: ')
