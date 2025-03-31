from CurrencyExchange import currencyExchange

#I was thinking of using unit tests but the exchange rates
#change daily. So a good amount of the functions would not be tested well.
#historicalExchangeRate would be fine as well as createGraph() as they can
#use dates recorded


##uncomment below to set API key and initialize class
##put you api in the apiKey variable

#apiKey = ""
##testing = currencyExchange()
##testing.setAPI(apiKey)

##testing each function below

##testing.statusAPI()
##testing.remaining()
##testing.totalUses()
##testing.usedAlready()
##print()
##testing.availableCurrency()
##print()
##testing.historicalExchangeRate("2022-01-01", "USD")
##print()
##testing.latestExchangeRate("USD")
##print()
##testing.convertMoney(100,"USD", "EUR")
##print()
##testing.convertMoney(100, "JPY", "EUR")
##print()
##testing.createGraph(["2025-02-01", "2025-03-01", "2025-01-01", "2025-03-28"], "USD", "JPY")
##print()
##testing.createGraphLastSixMonths("USD", "JPY")
