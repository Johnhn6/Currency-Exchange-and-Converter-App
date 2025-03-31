from CurrencyExchange import currencyExchange
import time
import sys

#should account for an exception when the api limit is reached
#but i do not know what exception will be raised and i have not
#reached the limit so it will be a future update

#decided to make a helper function since I wrote this
#statement many times

def exitingBreak(statement):
    if statement == "BACK":
        return True

#Initialization setup for currencyExchange Class, commands,
#and whether the API is set or not

running = currencyExchange()
commands = ["Exit", "Api", "Status", "Available Currencies", "Convert", "Latest Exchange Rate", "Historical Rate", "Six Month Graph", "Graph of Dates", "Command Information"]
apiSet = False

#prints start of program
print("Welcome to my currency exchange program. This was made by John Nguyen using the API from CurrencyExchangeAPI.com.")
print()

while True:
    #set your API
    if apiSet == False:
        print("Please type your API key. If you do not possess an API key, then please visit CurrencyApi.com in order to obtain one.")
        print("They have a free option. Please be exact in typing the key or copy and paste the code.")
        print("If you wish to exit the program, please type: Exit.")
        userAPI = input()
        exitUpperCase = userAPI.upper()

        if exitUpperCase == "EXIT":
            break

        running.setAPI(userAPI)
        #I tested it and it won't give an exception unless you do a command after setting it.
        #So we will do a command but will not print it, specifcally from a command that won't use up you daily limit.
        try:
            running.statusAPI()

        except:
            print("This is the wrong API key. Please type it in again.")
            #print statement below is to make it look more cleaner on the shell when running the script
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")

            print()
            apiSet = False
            continue #will do next loop of the while loop without doing the rest of the code below

        apiSet = True
        print("API key has been successfully set.")
        print()

    #Set of commands. Type back in any input, whenever you want to get back here.
    #Unless your API is not set or is cleared, you should end up here.
    print("Here is a list of commands you can do. Please type in the word for the command you would like.")
    print("For any input needed, except for this input, you can type Back to exit back to the list of commands.")
    print("For information of each command, please type: Command Information")
    print()

    for i in commands:
        print(i)
        
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    
    userInput = input()
    userInput = userInput.upper()
    
##    print(userInput) # for testing
    
    #Condition and Flow Control of your inputs for each command and if it is an incorrect command
    
    if userInput == "EXIT":
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        break

    
    elif userInput == "STATUS":
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        running.totalUses()
        running.usedAlready()
        running.remaining()
        

    elif userInput == "AVAILABLE CURRENCIES":
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        running.availableCurrency()

    #3 inputs since convertMoney() needs 3 parameters. Can type Back in any of them to go back to commands list. Will
    #be same for the inputs in the other conditionals statement blocks
    elif userInput == "CONVERT":
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        while(True):
            print("Please select base currency. Type Back anytime if you want to exit.")
            try:
                baseCurrency = input()
                baseCurrency = baseCurrency.upper()
                print()
                
                if exitingBreak(baseCurrency):
                    break

                print("Please select amount.")
                amount = input()
                amount = float(amount)
                print()
                if exitingBreak(amount):
                    break
            
                print("Please select currency to exchange to.")
                newCurrency = input()
                newCurrency = newCurrency.upper()
                if exitingBreak(newCurrency):
                    break
                running.convertMoney(amount, baseCurrency, newCurrency)
                break
            
            except:
                print("Currency or amount is incorrect or not supported. Please choose another one.")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------")

    #does latestExchangeRate()
    elif userInput == "LATEST EXCHANGE RATE":
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Please select currency. Type Back anytime if you want to exit.")
        exiting = False
        while True:
            try:
                currency = input()
                currency = currency.upper()
                if exitingBreak(currency):
                    exiting = True
                    break
                latest = running.latestExchangeRate(currency)
                break
            except:
                print("Currency is incorrect or not supported. Please choose another one. Type Back if you want to exit.")
        
        while True:
            if exiting == True:
                break
            try:
                print("Please select another currency to show latest exchange rate. Type Finish when you are done.")
                newCurrency = input()
                newCurrency = newCurrency.upper()
                
                if exitingBreak(newCurrency):
                    break
                elif newCurrency == "FINISH":
                    break
                
                print("Latest Rate for " + currency + " to " + newCurrency + " is " + str(latest[currency][newCurrency]["value"]) + ".")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------")
                print()
                
            except:
                print("Currency is incorrect or not supported. Please choose another one.")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------")

    #does historicalExchangeRate()
    #also does a loop where you can continuously input more historical exchange rates until you decide to Finish
    elif userInput == "HISTORICAL RATE":
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        while True:
            try:
                print("Please select currency. Type Back anytime if you want to exit.")
                currency = input()
                currency = currency.upper()
                print()
                if exitingBreak(currency):
                    break
                print("Please select date. Must be in year-month-day. Example: 2025-01-01.")
                date = input()
                dateFinish = date.upper()
                if exitingBreak(baseCurrency):
                    break
                dataset = running.historicalExchangeRate(date, currency)
                while True:
                    try:
                        print("Please select another currency to show exchange rate. Type Finish when you are done.")
                        newCurrency = input()
                        newCurrency = newCurrency.upper()
                        
                        if exitingBreak(newCurrency):
                            break
                        elif newCurrency == "FINISH":
                            break
                        
                        print("Rate on " + date + " for " + currency + " to " + newCurrency + " is " + str(dataset[(date, currency)][newCurrency]["value"]) + ".")
                        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
                        print()
                        
                    except:
                        print("Currency is incorrect or not supported. Please choose another one.")
                        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
                break
                    
            except:
                print("Currency or date is incorrect or not supported. Please choose another one.")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------")

    #does createGraphLastSixMonths()
    #You must exit the graph that gets displayed in order to continue the code
    #may try to fix this in the future
    elif userInput == "SIX MONTH GRAPH":
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Please select base currency. Type Back anytime if you want to exit.")
        while True:
            try:
                baseCurrency = input()
                baseCurrency = baseCurrency.upper()
                print()
                if exitingBreak(baseCurrency):
                    break
                
                print("Please select currency to exchange to.")
                newCurrency = input()
                newCurrency = newCurrency.upper()
                if exitingBreak(newCurrency):
                    break
                print("Please delete graph window before creating another graph.")
                running.createGraphLastSixMonths(baseCurrency, newCurrency)
                print()
                break

            except:
                print("Currency is incorrect or not supported. Please choose another one.")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------")

    #does createGraph()
    #when typing your dates, you can go back to command list by typing Back
    elif userInput == "GRAPH OF DATES":
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        while True:
            try:
                print("Please select base currency. Type Back anytime if you want to exit.")
                baseCurrency = input()
                baseCurrency = baseCurrency.upper()
                print()
                if exitingBreak(baseCurrency):
                    break
                
                print("Please select currency to exchange to.")
                newCurrency = input()
                newCurrency = newCurrency.upper()
                print()
                if exitingBreak(newCurrency):
                    break

                print("Please select dates. Can be in any order. Must be in year-month-day. Example: 2025-01-01.")
                dates = []
                exiting = False
                while(True):
                    print("Type in date or type Done to complete your list of dates. Type Finish when you are done.")
                    date = input()
                    
                    if date.upper() == "FINISH":
                        break
                    elif exitingBreak(date.upper()):
                        exiting = True
                        break
                    
                    dates.append(date)
                    print()

                #if you want to go back instead of finishing the graph then you should go back to commands instead
                #of creating the graph
                if exiting == True:
                    break
                
                print("Please delete graph window before creating another graph.")
                running.createGraph(dates, baseCurrency, newCurrency)
                
                print()
                break

            except:
                print("Currency or date is incorrect or not supported. Please choose another one.")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------")

    #"clears API, but really just sets apiSet back to false
    elif userInput == "API":
        print("API has been cleared.")
        apiSet = False

    #prints out the overview of what each command does
    elif userInput =="COMMAND INFORMATION":
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Exit: Exit the application.")
        print()
        print("Api: Clears API and allows you to select another API key.")
        print()
        print("Status: Shows status of API such as remaing uses if you have a monthly limit.")
        print()
        print("Available Currencies: Shows List of Currencies.")
        print()
        print("Convert: Converts one currency to another currency.")
        print()
        print("Latest Exchange Rate: Gives you the lastest exchange rate for a currency of your choosing.")
        print()
        print("Historical Rate: Gives you the exchange rate of one currecny to another on a specific date. Must be in Year-Month-Day format. Example: 2025-01-01")
        print()
        print("Six Month Graph: Gives you a graph of the exchange rate between two currencies of the last six months.")
        print()
        print("Graph of Dates: Gives you a graph of the exchange rate between two currencies using dates of your choosing.")
        

    #If the commmand is not there then try again. The any() is essentially a lambda expression as it checks any input to all the capitilized strings in my list
    #since I made the inputs all capitilized to account for users typing in the word with or without capitilization
    elif not any(command.upper() == userInput for command in commands):
        print("Sorry, but it seems your command is incorrect. Please type the word without any spaces. Do not worry about capitalization.")

    print("----------------------------------------------------------------------------------------------------------------------------------------------------")



#Decided to make exit actually end the program. Used time.sleep() to create a delay.
#Python should be able to clean up everything with their in-built garbarge disposal        

print("Thank you for using this program. Have a nice day!")
print("Program is now exiting.")
print("Please wait 3 seconds.")
time.sleep(3)
sys.exit()
