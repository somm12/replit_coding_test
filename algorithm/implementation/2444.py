n = int(input())
for i in range(n):
    for k in range(i,n-1):
        print(" ",end='')
    for k in range(0,i+1):
        print("*",end='')
    for k in range(0,i):
        print("*",end='')
    print()
    

for i in range(n-1):
    for k in range(i+1):
        print(" ",end='')
    for k in range(n-1,i,-1):
        print("*",end='')
    for k in range(n-2,i,-1):
        print("*",end='')
    print()