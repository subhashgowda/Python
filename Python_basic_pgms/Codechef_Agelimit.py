t = int(input("enter the testcases"))
while t>0:
    #X=int(input("enter minimum age"))
    #Y = int(input("enter the maximum age"))
    #A = int(input("enter the age of chef"))
    X,Y,A=map(int,input().split())
    print("Yes") if X<=A<Y else print("No")

    t=t-1

