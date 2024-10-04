t = int(input())

for i in range(t):
    n, x = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    maxDistance = arr[0]

    for i in range(1,n):
        distance = arr[i] - arr[i-1]
        maxDistance = max(maxDistance,distance)
    
    
    
    distanceOfLastToX = 2 * (x - arr[-1])

    if distanceOfLastToX > maxDistance:
        maxDistance += (distanceOfLastToX - maxDistance)
    
    print(maxDistance)
