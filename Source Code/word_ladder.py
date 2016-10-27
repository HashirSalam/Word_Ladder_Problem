import json 
import csv
from pprint import pprint
from pythonds.graphs import Graph
from pythonds.basic import Queue


with open('dict.json') as data_file:    
    data = json.load(data_file)         #Loading the Json File

keys = []
for k in data:
    keys.append(k)                     #Adding the words to a list 
    #print k

keys.sort()                            #Sorting the list in Aplphabatical order 
#for k in keys:
#    print k

def buildGraph(keys,length):
    d = {}
    g = Graph()
   
    #wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for k in keys:
        if(k.find('-') ==-1 and len(k) == length):      
            #word = k[:-1]
            word = k
            #print word          
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
    
    #for p in d['WEA_']:  Prints bucket 
    #    print p
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    
    return g

def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')


def traverse(y):
    x = y
    resultlist = []
    while (x.getPred()):
        #print(x.getId())
        resultlist.append(x.getId())    
        x = x.getPred()
    #print(x.getId())
    resultlist.append(x.getId())
    print resultlist 
    print "\nNumber of Chains: ",len(resultlist)-1
    return resultlist


def word_ladder(keys,size):
    graph = buildGraph(keys,size) #create a graph of words of letters==size
    word1 = raw_input("1st word: ")
    word1 = word1.upper()
    word2 = raw_input("2nd word: ")
    word2 = word2.upper()
    bfs(graph, graph.getVertex(word1))
    traverse(graph.getVertex(word2))  

def all_chains(keys,size):
    graph = buildGraph(keys,size) #create a graph of words of letters==size
    mylist = graph.getVertices()
    #print mylist
    for i in range(len(mylist)):
        graph2 = buildGraph(keys,size)     
        bfs(graph2, graph2.getVertex(mylist[i]))
        for j in range(i + 1, len(mylist)):
            #print ("FOR ",mylist[i] ," And " ,mylist[j])
            with open('result.csv', 'a') as csvfile:
                spamwriter = csv.writer(csvfile)
                blegh = traverse(graph2.getVertex(mylist[j]))
                #print blegh ,"Chain Lenght: ", len(blegh)-1
                result = blegh ,"Length: ", len(blegh)-1    
                spamwriter.writerow(result)
 

#graph = buildGraph(keys,4)
#graph2 = buildGraph(keys,15)
#pprint(graph2.getVertices())                           #VERY IMPORTANT 
#bfs(graph2, graph2.getVertex('NAVAL'))
#traverse(graph2.getVertex('GLIDE'))    

print("------ WELCOME TO WORD LADDER MAKER------- \n\n ")

while(True):
    size = raw_input("Please enter word length: ")
    size = int(size)  # change to int

    print("\nWhat would you like to do ?")
    print("(1)Find Word Ladder between any 2 words.\n(2)Find all the word ladders. (result stores in result.csv file)\n")
    
    choice = raw_input("Enter Choice Number:  ")
    choice = int(choice)  # change to int
    if(choice == 1):
        word_ladder(keys,size)
    elif (choice == 2):
        all_chains(keys,size)






         




