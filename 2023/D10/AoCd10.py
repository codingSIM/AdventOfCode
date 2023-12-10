#Day 10: Pipe Maze

#---Part 1------------------------------------------------------
##Based on the acoustics of the animal's scurrying, you're
##confident the pipe that contains the animal is one large,
##continuous loop.

##    | is a vertical pipe connecting north and south.
##    - is a horizontal pipe connecting east and west.
##    L is a 90-degree bend connecting north and east.
##    J is a 90-degree bend connecting north and west.
##    7 is a 90-degree bend connecting south and west.
##    F is a 90-degree bend connecting south and east.
##    . is ground; there is no pipe in this tile.
##    S is the starting position of the animal; there is
##      a pipe on this tile, but your sketch doesn't show
##      what shape the pipe has.

#arr[down][right] or [row][col].

with open("input10.txt") as f:
    lines = list(filter(None,f.read().split("\n")))

#First find S location

def find_location(start, arr):
    for i in range(0,len(arr)-1):
        if not (arr[i].find(start)==-1):
            return [i, arr[i].find(start)]

animal=find_location("S", lines)

print("Animal: ", animal)

#should always return 2 connections, as this is a closed loop
#this only works for first instance in case S as S is part of 1 loop
#It can be assumed there are only 2 connections. This will help determine
#the pipe shape of "S"
def get_start_connections(i, j, arr):
    #above
    conn=[]
    if arr[i-1][j]=="F" or arr[i-1][j]=="7" or arr[i-1][j]=="|":
        conn.append("up")
        
    #below
    if arr[i+1][j]=="L" or arr[i+1][j]=="J" or arr[i+1][j]=="|":
        conn.append("down")
        
    #left
    if arr[i][j-1]=="L" or arr[i][j-1]=="F" or arr[i][j-1]=="-":
        conn.append("left")
        
    #right
    if arr[i][j+1]=="7" or arr[i][j+1]=="J" or arr[i][j+1]=="-":
        conn.append("right")

    #print("Conn: ", conn)
    if len(conn)>2:
        print("LEngth: ",len(arr[i]))
        print("Something went wrong:", i , j)
        print(arr[i-1])
        print(arr[i])
        print(arr[i+1])

    return conn

def get_connections(i,j,arr):
    match arr[i][j]:
        case "|": return ["up", "down"]
        case "J": return ["up", "left"]
        case "L": return ["up", "right"]
        case "7": return ["down", "left"]
        case "F": return ["down", "right"]
        case "-": return ["left", "right"]

def start_pipe_shape(i, j, arr):
    match (get_start_connections(i, j, arr)):
        case ["up", "down"]: return "|"
        case ["up", "left"]: return "J"
        case ["up", "right"]: return "L"
        case ["down", "left"]: return "7"
        case ["down", "right"]: return "F"
        case ["left", "right"]: return "-"
    
lines[animal[0]]=lines[animal[0]].replace("S",start_pipe_shape(animal[0], animal[1], lines))



#For part 2-------------------------------------
linesloop=[]
arrpart2=[]
for i in range(0, len(lines)):
    line=[]
    line2=[]
    for j in range(0, len(lines[i])):
        line.append(0)
        line2.append(lines[i][j])
    linesloop.append(line)
    arrpart2.append(line2)

#-----------------------------------------------



def get_opposite(direction):
    match direction:
        case "up": return "down"
        case "down": return "up"
        case "left": return "right"
        case "right": return "left"

def loop(i,j,arr):
    global linesloop
    curri=i
    currj=j

    get2steps=get_connections(i, j, arr)
    #print("Both possible ways: ", get2steps)
    nextstep=get2steps[0]
    #print("First step: ",nextstep)
    match nextstep:
        case "up":curri-=1
        case "down":curri+=1
        case "left": currj-=1
        case "right": currj+=1
    count=1

    while not(curri==i and currj==j):
        get2steps=get_connections(curri,currj,arr)
        linesloop[curri][currj]=1

        oppositestep=get_opposite(nextstep)

##        a=["left", "right"]
##        if "left" in a:
##            a.remove("left")
##            b=a
##            #b=a.remove("left")
##        print(b)

        #remove other step, to get direction
        get2steps.remove(oppositestep)
        nextstep=get2steps[0]
        #print("Next step:", nextstep)
        match nextstep:
            case "up":curri-=1
            case "down":curri+=1
            case "left": currj-=1
            case "right": currj+=1
        count+=1
    return count
        
print("Answer part 1: ", int(loop(animal[0], animal[1], lines)/2)) #6725


#---Part 2------------------------------------------------------
#How many tiles are enclosed by the loop?

#https://mathsfromnothing.au/checking-if-a-point-is-inside-a-shape/?i=1

##^"One method that can be used to check if a point is inside any enclosed,
##non-self-intersecting shape in any number of dimensions is to draw a line
##in any direction away from the point and count the number of times the
##point crosses the boundary. If the line crosses an odd number of times
##the point is inside the shape. Note, the line begins at the point and
##extends to infinity on one side of the point, it does not pass through
##the point."

#arr1 is normal array
#arrloop is array of whether an item is part of loop or not
#we get 2 layers and use change_line, to dissolve horizontal lines

def change_line(arr1, arrloop):
    for i in range(0,len(arrloop)-1):
        previ=arrloop[i]
        if (previ==1 and arrloop[i+1]==1):
            match [arr1[i],arr1[i+1]]:
                case ["F", "-"]:
                    #becomes - F
                    arr1[i]="-"
                    arrloop[i]=2
                    arr1[i+1]="F"
                    arrloop[i+1]=1
                case ["F", "J"]:
                    #becomes - |
                    arr1[i]="-"
                    arrloop[i]=2
                    arr1[i+1]="|"
                    arrloop[i+1]=1
                case ["F", "7"]:
                    #becomes ||
                    arr1[i]="|"
                    arrloop[i]=1
                    arr1[i+1]="|"
                    arrloop[i+1]=1
                case ["L", "-"]:
                    #becomes -L
                    arr1[i]="-"
                    arrloop[i]=2
                    arr1[i+1]="L"
                    arrloop[i+1]=1
                case ["L", "7"]:
                    #becomes - |
                    arr1[i]="-"
                    arrloop[i]=2
                    arr1[i+1]="|"
                    arrloop[i+1]=1
                case ["L","J"]:
                    #becomes ||
                    arr1[i]="|"
                    arrloop[i]=1
                    arr1[i+1]="|"
                    arrloop[i+1]=1
    return arrloop    

#Part 2 loop and answer
count=0
for i in range(0,len(arrpart2)):
    checkline=change_line(arrpart2[i],linesloop[i])
    inside=False
    for x in checkline:
        if x==1:
            inside=not(inside)
        elif x==0 and inside:
            count+=1
        else:
            continue


print("Answer part 2: ", count) #383

