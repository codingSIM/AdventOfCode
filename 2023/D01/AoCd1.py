#Day 1: Trebuchet?!

with open("input1.txt") as f:
    lines = f.read().split("\n")

resultlines=[]
total=0

#function to stick 2 numbers together
# ex: "a" + "b" => "ab"
def combine(a,b):
    if a=="a" and b=="z":
        return(0)
    else:
        return(int(str(a)+str(b)))

#looping over all the lines
for i in (range(0,len(lines)-1)):
    #setting first,last digit to default a and z
    firstD="a"
    lastD="z"
    #looping over every character of each line
    for char in lines[i]:
        if char.isdigit():
            if (not(firstD.isdigit()) or not(lastD.isdigit())):
                firstD=char
                lastD=char
            else:
                lastD=char
    #adding each line's result into an array
    resultlines.append(combine(firstD,lastD))

#calculating part 1 answer
for x in resultlines:
    total+=x

print("Answer part 1: " + str(total))

#=====Part 2====================================================


total2=0
calibratedlist=[]
resultlines2=[]

#looping over each line of input
for k in (range(0,len(lines)-1)):
    test=lines[k]
    #replace each written number, with the digit
    #workaround for split cases such as "eighthree" strings
    test=test.replace("one", "o1e")
    test=test.replace("two", "t2o")
    test=test.replace("three", "t3e")
    test=test.replace("four", "f4r")
    test=test.replace("five", "f5e")
    test=test.replace("six", "s6x")
    test=test.replace("seven", "s7n")
    test=test.replace("eight", "e8t")
    test=test.replace("nine", "n9e")

    calibratedlist.append(test)

#looping over calibrated list
for j in (range(0,len(calibratedlist))):
    firstD="a"
    lastD="z"
    #same as part 1
    for char in calibratedlist[j]:
        if char.isdigit():
            if (not(firstD.isdigit()) or not(lastD.isdigit())):
                firstD=char
                lastD=char
            else:
                lastD=char

    resultlines2.append(combine(firstD,lastD))

#same as part 1
for x in resultlines2:
    total2+=x

print("Answer part 2: " + str(total2))
