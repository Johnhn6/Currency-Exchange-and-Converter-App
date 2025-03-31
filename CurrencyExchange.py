import currencyapicom

import numpy as np

import matplotlib.dates as mdates
import matplotlib.units as munits

import matplotlib.pyplot as plt

from datetime import datetime
from dateutil.relativedelta import relativedelta

#I checked the numbers and the calcutions are almost the same as the
#real time conversions with usually being off by a very small amount, depending
#on the size. The reason is that the rates we are getting is based on when
#it's updated and you must go to better subscription to get it minute per minute.
#But it is very close enough to get an accurate conversion.

class currencyExchange:
    #initializing any private variables the program will need, store, and manipulate for all its methods
    #storing the information can help with not overusing your daily limits with the api
    
    def __init__(self):
        self.apiKey = ""
        self.storedData = {}
        self.status = {}
        self.currencies = []
        self.latestExchange = {}
        self.latestDate = {}

        
    #For many APIs, they give you a key to access their library and applications.
    #For currencyapi.com, they can give you a free API key to use with a certain amoount of uses per month as well as a few
    #other restrictions. This method sets the API key.
        
    def setAPI(self, key):
        self.apiKey = key
##        print(self.apiKey)


    #The data structure that returns from the API is a dictionary. Inside the dictionary, there are values that have another dictionary.
    #Status API does not use up one of your monthly uses thankfully. It looks like this below. The worst case time scenario should be O(N).
    #{'account_id': 123456789123456789,
    # 'quotas': {'month': {'total': 300, 'used': 0, 'remaining': 300},
    # 'grace': {'total': 0, 'used': 0, 'remaining': 0}}}
    
    def statusAPI(self):
        client = currencyapicom.Client(self.apiKey)
        self.status = client.status()
        #print(self.status)
##        for i in self.status:
##            print(str(i) + " : " + str(self.status[i]))

    # These next 3 methods essentially look up our private status variable for the information we gain from statusAPI.
    # If you had not checked it yet, then they will call statusAPI. When you do a function that calls the statusAPI since it's empty,
    # then the program will do statusAPI().
    # Worst case time scenario for look up is O(1). If statusAPI() is called then it will be O(N).
    
    def remaining(self):
        if self.status == {}:
            statusAPI(self)
        print("Remaining uses: "+ str(self.status["quotas"]["month"]["remaining"]))

    def totalUses(self):
        if self.status == {}:
            statusAPI(self)
        print("Total uses: " + str(self.status["quotas"]["month"]["total"]))
    

    def usedAlready(self):
        if self.status == {}:
            statusAPI(self)
        print("Used already: " + str(self.status["quotas"]["month"]["used"]))


    #this function shows you the available currencies and prints it on each line
    #worst case time scenario is O(N)
        
    def availableCurrency(self):
        client = currencyapicom.Client(self.apiKey)
        if len(self.currencies) == 0:
            available = client.currencies()
            for i in available["data"]:
                self.currencies.append(i)
        for i in self.currencies:
            print(i)
            
        
    #Decided to make my private data variable be like an inverted index
    #this is in case you decide to do multiple historical exchange rates
    #and so we store for each date for each country
    #since the key value will be small in an inverted index it should
    #be easier to store and look up.
    #O(1) if you do not have to update storedData. O(N) if you do.
    #date must be in year-month-day form. Example: '2022-01-01'.
    #Data structure of exchangre rate we get from currencyapi.com is below.
    #USD will be the example but every key in the first nest will be a currency.
    #{(""USD"):
    #   {
    #   "meta":{"last_updated_at": "2025-01-01T23:59:59Z"},
    #   "data":
    #       {"AED":
    #           {"code": "AED"
    #           "value": 3.67306}
    #       There is one like above for each currency but we are doing only AED as an example.
    #   }
    #}
    #for self.storedData, the key is (date, currency) and the value
    #is the data part of the above dictionary. Please keep in mind
    #that each key in data is exchange rate from (date, currency) to the currency in data
    #example being USD on 2022-01-01 to AED has an exchange rate of 3.67.
    #I actually got confused on that when I was doing future functions.
    #Worst case time scenario should be O(1) as putting the dictionary to
    #a variable is essentially making a pointer that points to a memory location
    
    def historicalExchangeRate(self, date, currency):
        client = currencyapicom.Client(self.apiKey)
        if (str(date), currency) not in self.storedData:
            history = client.historical(str(date), base_currency = currency) #i believe it is essentialy a database lookup so should be O(1)
            self.storedData[(str(date), currency)] = history["data"]
        return self.storedData


    #lastest exchange rate. Will store it in order to save api key usage
    #Will also store the "last updated at". Higher subscription will
    #have updates per minutes.
    #UPDATE: I have decided to change it to an index as
    #the default value is USD and for conversion calculations I do need it to be with
    #other currencies as the base currency
    #self.latestExchange is similar to self.storedData, except the
    #key is just the currency, example is USD, as I do not need
    #to store a date as it is the most recent exchange rate update
    #Worst case time scenario is same as historical exchange rate
    
    def latestExchangeRate(self, currency):
        client = currencyapicom.Client(self.apiKey)
        if currency not in self.latestExchange:
            current = client.latest(base_currency = currency)
            self.latestExchange[currency] = current["data"]
            self.latestDate[currency] = current["meta"]["last_updated_at"][0:9]
        #print("Latest exchange rate of " + currency + " is at the value of " + str(self.latestExchange[currency]["value"]) + " on " + self.latestDate + ".")
        return self.latestExchange

    #I believe if you use the free api key you are actually not allowed to use
    #the convert methods. But since we do have the exchange rates of the latest date
    #we can caculate it ourselves. I was able to find this out by trial and error
    #and by reading the error information where I got "everapi.exceptions.NotAllowed.
    #Worst case time scenario should be O(1)
    
    def convertMoney(self, amount, currency, newCurrency):
        client = currencyapicom.Client(self.apiKey)
        if currency not in self.latestExchange:
            self.latestExchangeRate(currency)
        conversion = str(self.latestExchange[currency][newCurrency]["value"] * amount)
        print(str(amount) + " " + currency + " to " + newCurrency + " is " + conversion + " " + newCurrency + " on " + self.latestDate[currency] + ".")
        
    #create a graph with dates as x-axis and exchange rate at y-axis
    #dates is a list that we sort
    #Worst case time scenario should be O(N)
    def createGraph(self, dates, currency, newCurrency):
        x = []
        y = []
        dates.sort()

        #checks if you already have stored the date and currency exchange rate
        #and uses historicalExchangeRate() if not
        for i in dates:
            if (i,currency) not in self.storedData:
                self.historicalExchangeRate(i, currency)
            x.append(i)
            y.append(self.storedData[(i,currency)][newCurrency]["value"])
        
        xpoints = np.array(x)
        ypoints = np.array(y)
        plt.plot(xpoints, ypoints, marker = "o")
        plt.xlabel("Date")
        plt.ylabel("Exchange Rate")
        plt.title("Exchange Rate of " + currency + " to " + newCurrency)
        plt.show()

    #create a graph with dates as x-axis and exchange rate at y-axis
    #we use the current date and the previous 5 months as our dates
    #Worst case time scenario should be O(1)
    #Even though there is a for loop, it is actually O(1)
    #as the loop will always be 6 iterations. So N will be always
    #6 in O(N) and so it ends up being O(1)
    def createGraphLastSixMonths(self, currency, newCurrency):
        x = []
        y = []

        if currency not in self.latestExchange:
            self.latestExchangeRate(currency)
        if newCurrency not in self.latestExchange:
            self.latestExchangeRate(newCurrency)
        
        currentDate = self.latestDate[currency]
        date_format = "%Y-%m-%d"
        currentDatetime = datetime.strptime(currentDate, date_format)
        subtractingMonths = [5, 4, 3, 2, 1]

        
        for i in subtractingMonths:
            previousMonth = currentDatetime - relativedelta(months = i)
            correctDateFormat = previousMonth.strftime(date_format)
            x.append(correctDateFormat)
            if (correctDateFormat,currency) not in self.storedData:
                self.historicalExchangeRate(correctDateFormat, currency)
            y.append(self.storedData[(correctDateFormat,currency)][newCurrency]["value"])
            
        x.append(self.latestDate[currency])
        y.append(self.latestExchange[currency][newCurrency]["value"])
        
        xpoints = np.array(x)
        ypoints = np.array(y)
        plt.plot(xpoints, ypoints, marker = "o")
        plt.xlabel("Date")
        plt.ylabel("Exchange Rate")
        plt.title("Last Six Month Exchange Rate of "+ currency + " to " + newCurrency)
        plt.show()
        



#can later on have a drop down box like on google so you can select countries from that drop down box
