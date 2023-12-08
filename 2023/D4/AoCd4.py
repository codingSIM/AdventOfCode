#Day 4: Scratchcards

#---Part 1------------------------------------------------------
##As far as the Elf has been able to figure out,
##you have to figure out which of the numbers you
##have appear in the list of winning numbers.
##The first match makes the card worth one point
##and each match after the first doubles the point
##value of that card.

##How many points are they worth in total?



with open("input4.txt") as f:
    lines = f.read().split("\n")

cleanArr=[]#final array of all scratchcards, but in a more usable form

for i in (range(0, len(lines)-1)):
    clean=[]
    idcards=lines[i].split(":")

    idc=(idcards[0].replace("Card","")).replace(" ","")
    clean.append(idc)

    #clean cards into 2 arrays, first array of winning cards,
    #second the array of your numbers
    winhave=(idcards[1].split("|"))

    #https://www.tutorialspoint.com/How-to-remove-empty-strings-from-a-list-of-strings-in-Python
    winnrs=list(filter(None, winhave[0].split(" ")))
    havenrs=list(filter(None, winhave[1].split(" ")))

    clean.append(winnrs)
    clean.append(havenrs)

    #print(clean)
    cleanArr.append(clean)


total=0
#calculating points total for all scratchcards
for i in range(0,len(cleanArr)-1):
    #how many times each scratchcard has won
    countWin=0
    for winnr in cleanArr[i][1]:
        
        for gotnr in cleanArr[i][2]:
            #if you have a number from the winning array
            #increase the count of wins for the scratchcard
            if winnr==gotnr:
                countWin+=1

    if countWin==0:
        total+=0
    else:
        #starting with 1 point,
        #for every win point you get to double the points of the scratchcards
        #powers of 2
        total+=(pow(2,countWin-1))

                
print(total)
#(Answer=28750)




#---Part 2------------------------------------------------------
##Process all of the original and copied scratchcards until
##no more scratchcards are won. Including the original set
##of scratchcards, how many total scratchcards do you end
##up with?


#Copies of scratchcards are scored like normal scratchcards
#and have the same card number as the card they copied. So,
#if you win a copy of card 10 and it has 5 matching numbers,
#it would then win a copy of the same cards that the original
#card 10 won: cards 11, 12, 13, 14, and 15. This process
#repeats until none of the copies cause you to win any more cards.

#(Cards will never make you copy a card past the end of the table.)
#--------------------------------------------------------------------

#function to get the nr of matches from scratchcards, given a cleanarr item.
def getMatches(arr):
    count=0
    for winnr in arr[1]:
        for gotnr in arr[2]:
            if winnr==gotnr:
               count+=1

    return count

#infinite loop test
##arr=[1,2,3,4,5]
##for x in arr:
##    print(x)
##    arr.append(x)

#start with the entire array of scratchcards
extracards=cleanArr

#Extra check + debugging
##for x in extracards:
##    print("Card ", x[0], "Matches: ", getMatches(x))


def endcards():
    #extracards.append(arr)
    for x in extracards:
        #print(x[0])
        m=getMatches(x)
        
        if m>0:
            for y in range(int(x[0]), int(x[0])+m):
                extracards.append(cleanArr[y])
        
    return len(extracards)

#Patience, this took 2 min to run
#Answer: 10212704
print(endcards())



