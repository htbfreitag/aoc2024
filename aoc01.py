#part 1
listA = []
listB = []

with open("list.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        line = line.split("   ")
        listA.append(int(line[0]))
        listB.append(int(line[1]))

listA.sort()
listB.sort()

theDifference = 0
index = 0

for item in listA:
    theDifference = theDifference + abs(listA[index] - listB[index])
    index+=1

print(theDifference)

#part 2
similarity = 0

for value in listA:
    if value in listB:
        similarity = similarity + abs(value * listB.count(value))
print(similarity)