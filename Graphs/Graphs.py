from collections import deque
grafo={}
grafo["Voce"]=["Alice","Bob","Claire"]
grafo["Bob"]=[]
grafo["Alice"]=["Peggy","Claire"]
grafo["Claire"]=["Thom","Jonny"]
grafo["Peggy"]=["Daniel"]
grafo["Thom"]=["Petter"]
grafo["Jonny"]=["Anuj"]
grafo["Jonny"]=[]
grafo["Anuj"]=[]

sellers=["Thom"]
def personIsSeller(name):
    if name in sellers:
        return True
    else:
        return False
def search(name):
    searchQueue=deque()#It creates a queue
    searchQueue+=grafo[name]#Add the list in the queue
    verified=[]
    while searchQueue:
        person=searchQueue.popleft()#Get a person in the queue
        if not person in verified:#If the person wasnt verified before
            if (personIsSeller(person)):#Verify if the current person is a seller
                print(f"{person} é um vendedor de manga!")
                return True
            else:#If the current person isnt a seller
                searchQueue+=grafo[person]#Add the contacts of the person in the queue
                verified.append(person)#Add the person in the list of verified
                print(searchQueue)
                print(verified)
search("Voce")