
while 1:
    n = int(input()) # 1<= n <= 10
    totalDistance = 0
    old_t = 0
    if n==-1:
        break
    elif 1<=n and n<= 10:
        for i in range(n):
            s, t = (input().split())
            s = int(s)
            t = int(t)
            if ( (1<=s) and (s<=90) ) and ( (1<=t) and (t<=12) ):
                totalDistance = totalDistance + (s * (t - old_t))
                old_t = t 
                #print("Loop No: " + str(i))
                #print("s: " + str(s))
                #print("old_t: " + str(t))
                #print("timetaken: " + str(old_t))

            #print(s)
        print (str(totalDistance) + " miles")

