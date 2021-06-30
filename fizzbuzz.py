a = input()
aList = a.split(" ")
X = int(aList[0])
Y = int(aList[1])
N = int(aList[2])




if ( (X>=1) and (X<Y) and (Y<=N) and (N<=100) ):

    for i in range(1,N+1):
        # print(i)
        if ( (i % X == 0) and (i % Y == 0) ):
            print('FizzBuzz')
        elif i % X == 0:
            print('Fizz')
        elif i % Y == 0:
            print('Buzz')
        else:
            print(i)
else:
    print('mumless')