import requests
import json
sesh = requests.Session()
from operator import itemgetter, attrgetter
import pyperclip
from caesarcipher import CaesarCipher


oldList = [['oof123', '123456', '105'], ['oof1234', '1234567', '65']]




team = "LB"



usernames = []
userids = []
races = []
raceIndividual = []
newList = []
def generateList():
    teamMembers = []
    teamURL = sesh.get("https://www.nitrotype.com/api/teams/" + team)
    parsed = teamURL.json()["data"]["members"]
    for x in parsed:
        usrn = x["username"]
        uid = str(x["userID"])
        usernames.append(usrn)
        userids.append(uid)
    for x in range(len(userids)):
        playerLink = "https://www.nitrotype.com/api/players/" + userids[x]
        playerGet = requests.get(url = playerLink)
        racingStats = playerGet.json()["data"]["racingStats"]
        if(len(racingStats) >= 2):
            races.append(str((racingStats[1]["played"])))
        else:
            races.append(str(0))

    for i in range (len(userids)):
        userList = []
        userList.append(usernames[i])
        userList.append(userids[i])
        userList.append(int(races[i]))
        teamMembers.append(userList)
    
    teamMembers = sorted(teamMembers, key=itemgetter(2), reverse = True)
    print(teamMembers)
    pyperclip.copy(str(teamMembers))
    return(teamMembers)

def compareList(teamMembers):
    for i in range(len(oldList)):
        for x in range(len(teamMembers)):
            if(str(teamMembers[x][0]) in oldList[i]):
                memberName = str(teamMembers[x][0])
                memberUserID = str(teamMembers[x][1])
                memberRaces = str(teamMembers[x][2])
                memList = []
                memList.append(memberName)
                memList.append(memberUserID)
                memList.append(memberRaces)
                newList.append(memList)
    print("hi")
    print(oldList)
    print("bye")
    for old in oldList:
        for new in newList:
            if(str(old[1]) == str(new[1])):
                new[2] = int(new[2]) + int(old[2])
   # for i in range (len(newList)):
   #     for x in range(len(oldList)):
    #        if(str(newList[i][1]) == str(oldList[x][1])):
     #           newList[i][2] = (int(newList[i][2]) + int(oldList[x][2]))

    sortedList = sorted(newList, key=itemgetter(2), reverse = True)
#sortedList = sorted(newList, key = lambda race: race[2])
    print(sortedList)
    pyperclip.copy(str(sortedList))

print("Enter team Name")
team = input()
print("Enter OLD list")
oldList = input()
oldList = eval(oldList)

print("Press y to generate new competition, press x to add to updated list.")
ans = input()

if(ans == "y"):
    generateList()
    print("copied to clipboard!")
if(ans == "x"):
    a = generateList()
    compareList(a)
    print("Copied to clipboard!")