t = int(input("enter the testcases"))
while t>0:
    X,Y,A=map(int,input().split())
    print("Yes") if X<=A<Y else print("No")

    t=t-1

