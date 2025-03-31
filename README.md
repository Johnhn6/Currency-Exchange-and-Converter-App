# Currency-Exchange-and-Converter-App
Using currencyapi.com's api, the application is able to show the lastest exchange rates, past exchange rates, convert currencies to another currency, and display graphs.


# How to Use
To use the program, please make sure to have python and to pip install currencyapicom. If you do not have python then please install python first. If you do not have pip install, then go to your command line by typing cmd in the file search bar, then type python -m pip install. Then write pip install currencyapicom. After that, go to currencyapi.com and get a free API key. Then you can run Main.py, where it will ask you for the API key. If you are going to use the testing file, then you must set your API key to the apiKey variable.


# Overview of Programs and Uses
There are 2 files for the program and a testing file. The program is in Main.py and CurrencyExchange.py, and the testing file is TestingCurrencyExchange.py. I utilized the API from currencyapi.com, and I hoped it showcased good use of understanding documentaion, using outside libraries, understand how
APIs work, and the use of object oriented programming in order to manipulate data within objects and data structures in order to perform the necessary functions of the application.

The testing files utilizes print states in order to test out each function. Originally, I was thinking of using unit tests, but the database updates quite frequently. So my unit tests would only really work with the historical data, which would cut a good amount of my tests. In the end, I checked if each function was returning or printing the correct information and that the calculations were correct. For Main.py, edge cases were tested such as using incorrect date format. By the end, I was satisfied with the testing.

In CurrencyExchange.py, I decided to create a class object that will utilize currencyapi.com's API and imported a few other libraries such as mathplotlib and numpy, as these other libraries were useful in my graph creating methods. The application is able to show the status of your API, show available currencies calculate the conversion of a currency to another currency, plot graphs with dates of your choosing or the last six months, and is able to show the latest or previous exchange rates of different currencies.

In Main.py, I decided to make this file be the user interface. It initializes the currencyExchange class and utilizes user input in order to navigate different
functions of the program. It has the function to go back to the command list for every input. In addition, I tried to make it as informative as possible so that the user understands their options. It can also catch certain exceptions such as wrong dates, incorrect currency, and incorrect amount. Finally, when you exit the user input, I wanted to emulate closing an application, so I made it wait a few seconds and then it will close the application. Though the python shell will remain.

I believe my application will be useful in calculating any conversions you need to different currencies. An example would be if you are traveling to Japan or to any EU country, then converting your currency to either JPY or EUR would be helpful. In addition, by showing a graph to see fluctuation of the currency exchange overtime, I hope it would useful in having a visualization of strength of each currency and it's use for any research purposes. 

One minor note to acknowledge would be the the exchange rate updates. When I tested the calculations, the amount is almost the same as other sites with only a few numbers or percent off. The reason is that the free API key will not have exchange rates minute by minute. So this would mean that the rates will be slightly off, but it will show you the overall rate of that day. Higher subscription will allow for minute by minute updates, which I believe my program will be able to do. The calculation from one currency to another is by multiplying the currency by the exchange rate to get the new currency. An example would be: USD * exchange rate to JPY = JPY.

# Potential Future Updates
- Creation of a front end application in either android studios or using javascript and html.
- Exception raised if you go beyond your limit. I did not make one as I did not go beyond the monthly limit
- Being able to use dates in other formats.


# Thank You
Special thanks to currencyapi.com for allowing use of their API with a free monthly option. This program is not meant to be for profit and is meant for personal use.
