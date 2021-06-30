strNum = input()
a, b, c = strNum.split(' ')
a = int(a)
b = int(b)
c = int(c)
if (a>=1 and a<=500) and (b>=1 and b<=500) and (c>=1 and c<=500):
    totalDesigns = a * b * c
    print(totalDesigns)
else:
    print("error input")
