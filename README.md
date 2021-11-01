"""
This program allows for an input of a specific stock ticker or company name,
and uses multiple API's to pull a daily closing price as well
as the leading news stories that might be applicable to the company.
If the change in closing price of the stock after the day is greater than 5%,
the script will use twilio to send a text message from a spoofed number to a number
the user is responsible for entering that contains the percentage change as well as
a title and description for the 3 most popular news articles for the comapny.
"""

"""
Default values consist of the following:
Stock/Company = Tesla Inc (Ticker: TSLA)
"To" phone number: My personal phone.
"""

"""
It should be noted this script will only successfully run on Tuesday-Friday as it uses
the datetime module to find the difference between yesterdays closing price and today's.
Since the market closes on the weekend, it cannot be run on Saturday, Sunday, or Monday.
"""
