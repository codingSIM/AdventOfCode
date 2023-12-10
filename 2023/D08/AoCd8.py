#Day 8: Haunted Wasteland

from math import gcd

#---Part 1------------------------------------------------------
with open("input8.txt") as f:
    lines = list(filter(None,f.read().split("\n")))

instructions = lines[0]

#remove first item list
lines.pop(0)

#Array1 = for name / location
name=[]
#Array2 = options L/R
optionsLR=[]
for i in range(0, len(lines)):
    arrboth=lines[i].replace(" ","").split("=")
    name.append(arrboth[0])
    optionsLR.append(arrboth[1].replace("(", "").replace(")","").split(","))

curr="AAA"
countAZ=0

#Sanity check, website example
##instructions="LLR"
##name=["AAA","BBB","ZZZ"]
##optionsLR=[["BBB","BBB"],["AAA","ZZZ"],["ZZZ","ZZZ"]]

#function to find index of location


def findLocationIndex(n, arr):
    for j in range(0,len(arr)):
        if arr[j] == n:
            return j
            
#function to follow instructions
def followInstructions():
    #https://docs.python.org/3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value
    global curr, countAZ

    while not (curr == "ZZZ"):
        for char in str(instructions):
            index=findLocationIndex(curr, name)
            #print("Count: ", countAZ, "Index: ",index, "Name: ", curr)
            countAZ+=1
            if char == "L":
                curr=optionsLR[index][0]
                #countAZ+=1
                
            else:
                curr=optionsLR[index][1]
                #countAZ+=1
            #print("Index is: ", index, " curr: ", curr, " Count: ", countAZ, " CHAR: ", char)

        
        #print(curr, countAZ)
        #break
    return(countAZ)


print("Answer part 1: ", followInstructions()) #17621

#print(str(instructions))

#---Part 2------------------------------------------------------

#let's find all nodes ending in A
startNodes=[]
for i in range(0,len(name)):
    if name[i][-1]=="A":
        startNodes.append(name[i])

#print(findLocationIndex("HGL", name))
print("Start nodeS: ", startNodes)


##currNodes=startNodes
##countXXZ=0
##terminate=0

##Although this would work, it won't work in a reasonable time
#====First try==========================================================
##def concurentlyFollowInstructions():
##    global currNodes, countXXZ, terminate
##    while True:
##        terminate=0
##        for x in range(0,len(currNodes)):
##            for char in str(instructions):
##                index=findLocationIndex(currNodes[x], name)
##                if char == "L":
##                    currNodes[x]=optionsLR[index][0]
##                    
##                else:
##                    currNodes[x]=optionsLR[index][1]
##            
##        countXXZ+=1
##        #they concurrently reach a destination of form XXZ
##        for x in currNodes:
##            if x[-1]=="Z":
##                terminate+=1
##                #print(countXXZ)
##                
##            elif terminate==len(currNodes):
##                return countXXZ
##            
##        #print(currNodes)
##print(concurentlyFollowInstructions())

#---Part 2: try 2------------------------------------------------------
#Instead of waiting for all the iterations to be done and all
#starting points to end in Z, if I find out the time/counts it
#takes for them to get to Z, I can then find the LCM of all
#these counts, to find the total steps it takes for all to
#reach XXZ at the same time.
def getRepeatCount(start):
    count=0
    #print((start[-1]))
    while not (start[-1]=="Z"):
        for char in str(instructions):
            index=findLocationIndex(start, name)
            count+=1
            if char == "L":
                start=optionsLR[index][0]
            else:
                start=optionsLR[index][1]
    #print(start, count)
    return count

LCM=[]
for x in startNodes:
    #print(x)
    LCM.append(getRepeatCount(x))

#https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python
lcm=1
for i in LCM:
    lcm=lcm*i//gcd(lcm,i)
print("Answer part 2: ", lcm)
