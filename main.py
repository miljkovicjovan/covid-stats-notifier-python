import os 
import requests
from plyer import notification
import datetime
import time

covidData = None

try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/serbia")
except:
    #if no data fetched
    print("Please! Check your internet connection")

#if we have data create notification
if (covidData != None):
    #converting data to JSON format
    data = covidData.json()['Success']

    while True:
        #notification
        notification.notify(
            #title
            title = "COVID Stats on {}".format(datetime.date.today()),
            #body
            message = "Total cases : {totalcases}\nToday cases: {todaycases}\nToday deaths: {todaydeaths}\nTotal active: {active}".format(
                totalcases = data['cases'],
                todaycases = data['todayCases'],
                todaydeaths = data['todayDeaths'],
                active = data['active']),
            #icon for the notification
            #we need ico format
            app_icon = "bell.ico",
            #how long the notification stays before automatically deletes
            timeout = 50
        )
        #notification to repeat every 4hrs
        #60secs times 60mins times 4 for 4 hrs total
        time.sleep(60*60*4)