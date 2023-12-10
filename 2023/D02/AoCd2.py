#Day 2: Cube Conundrum

#---Part 1------------------------------------------------------------------
#Determine which games would have been possible if the bag
#had been loaded with only 12 red cubes, 13 green cubes,
#and 14 blue cubes.

#What is the sum of the IDs of those games?


with open("input2.txt") as f:
    lines = f.read().split("\n")

cleanArr=[]

#Splitting/Cleaning input into more useful bits
for i in (range(0,len(lines)-1)):
    #cleanLine=[id, [[x red], [y blue], [z green]], [etc...]]
    cleanLine=[]
    
    idGame=lines[i].split(":") #split id and games
    
    ida=idGame[0].replace("Game ","") #int id
    cleanLine.append(ida) #add int
    
    games=idGame[1].split(";") #split games
    for j in (range(0,len(games))):
        g=games[j].split(",")
        for h in (range(0,len(g))):
            #strip cleans it of extra spaces on left or right of string
            g[h]=g[h].strip()
            
        cleanLine.append(g) #append each set from game[i]
        
    cleanArr.append(cleanLine) #add each cleanLine to cleanArr

#Part 1
#Which games would have been possible if the bag contained
#only 12 red cubes, 13 green cubes, and 14 blue cubes?

total=0 #answer part 1 (2879)
for k in (range(0,len(cleanArr))):
    #print(cleanArr)
    idat=int(cleanArr[k][0])
    addId="true"

    for l in range(1,len(cleanArr[k])):
        g=cleanArr[k][l] #one of the games
        for m in g:
            m=m.split(" ")
            if m[1] == "red" and int(m[0])>12:
                addId = "false"
            elif m[1] == "blue" and int(m[0])>14:
                addId="false"
            elif m[1] == "green" and int(m[0])>13:
                addId = "false"
    if addId=="true":
        total+=idat

print(total)


#---Part 2----------------------------------------------------------
#In each game you played, what is the fewest number
#of cubes of each color that could have been in the
#bag to make the game possible?

# => find maximum nr in each game of each colour

#For each game, find the minimum set of cubes that
#must have been present. What is the sum of the
#power of these sets?

total2=0 #answer part 2 (65122)
for k in (range(0,len(cleanArr))):
    #r,v,b maximum default is 0
    r,v,b=0,0,0

    for l in range(1,len(cleanArr[k])):
        g=cleanArr[k][l] #one of the games
        for m in g: #finding max for each colour in each game
            m=m.split(" ")
            if m[1] == "red" and int(m[0])>r:
                r=int(m[0])
            elif m[1] == "blue" and int(m[0])>b:
                b=int(m[0])
            elif m[1] == "green" and int(m[0])>v:
                v=int(m[0])
    #The power of a set of cubes is equal to the
    #numbers of red, green, and blue cubes multiplied together.
    power=r*v*b
    total2+=power

print(total2)


            
