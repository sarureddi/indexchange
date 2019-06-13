n1=int(input())
ao1=list(map(int,input().split()))
for i1 in range (0,n1-1):
    if(ao1[i1]!=i1+1):
        print(i1)
        break
