import requests
from bs4 import BeautifulSoup

def findPlayer(player):
    ##Open results of searched player
    playerF = player.replace(" ", "_")
    url = f"https://liquipedia.net/smash/{playerF}/Results"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    ##Return number of first place finishes
    firsts = soup.find_all('td', class_='placement-1')
    firstPlace = len(firsts)
    return firstPlace

##Recieve user input
player = input("Enter a player: ")

##Show results
firstPlace = findPlayer(player)
print(f"{player} has finished first {firstPlace} times.")