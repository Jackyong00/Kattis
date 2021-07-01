# str1 = ''.join(a)
#print(listOfScore)
largestNumber = 0
largestLine = 0
for i in range(1,6):
    lineTotalScore = 0
    listOfScore = input().split()
    #print(listOfScore)
    for j in listOfScore:
        #print(j)
        lineTotalScore = lineTotalScore + int(j)
    if lineTotalScore > largestNumber:
        largestNumber = lineTotalScore
        largestLine = i
        #print(i)

        
        # totalScore = int(totalScore) + listOfScore[int(i)]

print("{} {}".format(largestLine,largestNumber))
