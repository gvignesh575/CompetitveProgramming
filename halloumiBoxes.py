t = int(input())

for i in range(t):
    n, k = list(map(int,input().split()))
    arr = list(map(int,input().split()))

    isSorted = True 
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            isSorted = False
        
    if isSorted == True:
        print("YES")
        
    else:
        if k <= 1:
            print("NO")
        else:
            print("YES")
