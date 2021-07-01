numOfConstant = int(input())
#q, y = input().split()
totalQALY = 0
for i in range(numOfConstant):
    q, y = input().split()
    qaly = float(q) * float(y)
    totalQALY = totalQALY + qaly
print(totalQALY)

