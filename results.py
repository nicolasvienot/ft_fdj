# Import libraries
from datetime import datetime
import requests
import urllib.request
from bs4 import BeautifulSoup

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

#LOTO
# Set the URL you want to webscrape from
url = 'https://www.fdj.fr/jeux-de-tirage/loto/?jeu=loto'

# Connect to the URL
response = requests.get(url)

# print(response)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# print("soup ", soup)

soup.find("div", {"id": "articlebody"})

loto = ""
test = 0
for div in soup.find_all('div', {"class":"numbers-item"}):
    # print (div.span.contents[0])
    if test == 0:
        loto = div.span.contents[0]
        test = 1
    else:
        loto = loto + " " + div.span.contents[0]

for div in soup.find_all('div', {"class":"drawing-infos_title"}):
    test = test + div

dateloto1 = soup.find('h1', {"class":"drawing-infos_title"})
dateloto = dateloto1.contents[0]

#EUROMILLION

url = 'https://www.fdj.fr/jeux-de-tirage/euromillions-my-million/resultats'

# Connect to the URL
response = requests.get(url)

# print(response)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# print("soup ", soup)

soup.find("div", {"id": "articlebody"})

euromil = ""
test = 0
for div in soup.find_all('div', {"class":"numbers-item"}):
    # print (div.span.contents[0])
    if test == 0:
        euromil = div.span.contents[0]
        test = 1
    else:
        euromil = euromil + " " + div.span.contents[0]

dateeuro1 = soup.find('h1', {"class":"drawing-infos_title"})
dateeuro = dateeuro1.contents[0]

RESULTS = { 
    "Loto": {
        "type":"loto",
        "nums": loto,
        "date-tirage":dateloto,
        "timestamp": get_timestamp()
    },
    "Euromillion": {
        "type":"euromillion",
        "date-tirage":dateeuro,
        "nums": euromil,
        "timestamp": get_timestamp()
    }
}

def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [RESULTS[key] for key in sorted(RESULTS.keys())]