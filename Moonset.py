from bs4 import BeautifulSoup
import urllib.request
import time
import re


def replay():
    time.sleep(1)
    another_day = input("Wanna check another day? Please enter Y or N ")
    if another_day is "Y":
        get_moonset()
    elif another_day is "N":
        quit()
    else:
        print("Please enter Y or N")
        replay()


def get_moonset():
    # setup the source
    with urllib.request.urlopen("https://www.timeanddate.com/moon/usa/tampa") as url:
        req = url.read()
    # get the data
    soup = BeautifulSoup(req, "html.parser")
    # setup a dictionary
    msets = {}
    # look for the string to find the data
    title = re.compile("^The Moon sets ")
    # for loop to extract and assign the data
    for row in soup.table.tbody.find_all('tr'):
        day = row['data-day']
        mset = row.find(title=title)
        if day and mset:
            msets[day] = mset.get_text()
    # setup a dictionary
    illum = {}
    # look for the string to find the data
    title1 = re.compile("^The Moon's disk ")
    # for loop to extract and assign the data
    for rows in soup.table.tbody.find_all('tr'):
        days = rows['data-day']
        illuminate = rows.find(title=title1)
        if days and illuminate:
            illum[days] = illuminate.get_text()
    # input for the date the user wants
    what_date  =input("Please enter a date for this month: ")
    # if the date entered is within the parameters of the month it'll print
    if what_date in msets and illum:
        print("The moon will set at " + msets[what_date] + ". It will be illuminated " + illum[what_date])
    else:
        print("There is no Moonset listed for this day.")
    # replay the get_moonset() function
    replay()


get_moonset()

