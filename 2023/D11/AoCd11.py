#Day 11: Cosmic Expansion

#---Part 1------------------------------------------------------
#The researcher has collected a bunch of data and compiled the
#data into a single giant image (your puzzle input). The image
#includes empty space (.) and galaxies (#). For example:

#The researcher is trying to figure out the sum of the lengths
#of the shortest path between every pair of galaxies.

#However, there's a catch: the universe expanded in the time it
#took the light from those galaxies to reach the observatory.

with open("input11.txt") as f:
    lines = list(filter(None,f.read().split("\n")))

arr=[]
arr2=[]
for x in lines:
    arr.append(list(x))
    arr2.append(list(x))


expandRow=[]
expandCol=[]
def expand_universe(array):
    global expandRow, expandCol
    countr=0
    countc=0
    for i in range(0,len(array)):
        for j in range(0,len(array[0])):
            if array[i][j]==".":
               countr+=1
               if countr==len(array[0]):
                   expandRow.append(i)
        countr=0
    for i in range(0,len(array[0])):
        for j in range(0,len(array)):
            if array[j][i]==".":
                countc+=1
                if countc==len(array[j]):
                    expandCol.append(i)
        countc=0

    #reverse arrays so that you can expand easier
    for x in expandRow[::-1]:
        array.insert(x,array[x])
        
    for y in expandCol[::-1]:
        for i in range(0,len(array)):
            array[i].insert(y,".")
    return array

expanded=expand_universe(arr)



##--Check------------------

#print(array[47])
#print(array[48])

def print_col(nr,array):
    l=[]
    for j in range(0,len(array[0])):
        l.append(array[j][nr])
    return print(l)

#print_col(2,array)
#print_col(3,array)
#--------------------------



def location_assign_number(array, symbol):
    count=0
    locations=[]
    for i in range(0,len(array)):
        for j in range(0,len(array[0])):
            if array[i][j] == symbol:
                count+=1
                array[i][j]=count
                locations.append([i,j])
    #print("Nr galaxies: ", count)
    return locations

galaxiesLoc=location_assign_number(expanded, "#")




#get all pairs
def get_combinations(array):
    res = [[a, b] for idx, a in enumerate(array) for b in array[idx + 1:]]
    #print(res)
    return res


pairs=get_combinations(galaxiesLoc)

countDist=0
for x in pairs:
    dist=0
    ##[[[0,27],[0,141]], ...
    ##0,4 and 2,0 => 2+4=6 shortest path
    dist+=abs(x[0][0]-x[1][0])+abs(x[0][1] - x[1][1])
    countDist+=dist

print("Answer part 1: ", countDist) # 9418609



#---Part 2------------------------------------------------------

#Now, instead of the expansion you did before, make each empty
#row or column one million times larger.

offset=999999

noOffsetGalaxiesLoc=location_assign_number( arr2, "#")


##Offsetting the locations
for x in range(0, len(noOffsetGalaxiesLoc)):
    xi=0
    xj=0
    for i in expandRow:
        if noOffsetGalaxiesLoc[x][0]>i:
            xi+=1
    for j in expandCol:
        if noOffsetGalaxiesLoc[x][1]>j:
            xj+=1

    noOffsetGalaxiesLoc[x][0]+=(xi*offset)
    noOffsetGalaxiesLoc[x][1]+=(xj*offset)



pairsOffset=get_combinations(noOffsetGalaxiesLoc)

offDist=0
for x in pairsOffset:
    dist=0
    ##[[[0,27],[0,141]], ...
    ##0,4 and 2,0 => 2+4=6 shortest path
    dist+=abs(x[0][0]-x[1][0])+abs(x[0][1] - x[1][1])
    offDist+=dist

print("Answer part 2: ", offDist) #593821230983











