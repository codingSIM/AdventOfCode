#Day 6: Wait For It

#---Part 1------------------------------------------------------
#You get your puzzle input, that lists the time allowed for
#each race and also the best distance ever recorded in that race
#To win the grand prize, you need to make sure you go farther
#than the current record holder.


##The boats are much smaller than you expected - they're actually
##toy boats, each with a big button on top. Holding down the button
##charges the boat, and releasing the button allows the boat to move.
##Boats move faster if their button was held longer, but time spent
##holding the button counts against the total race time. You can only
##hold the button at the start of the race, and boats don't move until
##the button is released.

#Your toy boat has a starting speed of zero millimeters per millisecond.

#For each whole millisecond you spend at the beginning of the race
#holding down the button, the boat's speed increases by one millimeter
#per millisecond.

#Determine the number of ways you can beat the record in each race.
#What do you get if you multiply these numbers together?

lines=open("input6.txt").read().split("\n")

#cleaning the lists
time=list(filter(None,lines[0].replace("Time:","").split(" ")))
dist=list(filter(None,lines[1].replace("Distance:","").split(" ")))

print(time)
print(dist)

ansArr=[]

#loop over each race
for race in range(0,len(time)):
    count=0
    #x in range of time
    for x in range(0,int(time[race])):
        #calculate time left, as time holding button doesn't count
        tleft=int(time[race])-x
        speed=x
        #dist=speed*time
        newdist=speed*tleft
        if newdist>int(dist[race]):
            count+=1
    ansArr.append(count)

print(ansArr)

#mt = multiplicative total
mt=1
for a in ansArr: mt*=a
print("Answer is: ", mt) #1710720




#---Part 2------------------------------------------------------
#Due to bad kerning, there is actually only one race
#! ignore the spaces between the numbers on each line

time=int(lines[0].replace("Time:","").replace(" ",""))
dist=int(lines[1].replace("Distance:","").replace(" ",""))

count=0
#same as part 1
for x in range(0, time):
    tleft=time-x
    speed=x
    currDist=speed*tleft
    if currDist>dist:
        count+=1

print("Answer is: ", count) #35349468
