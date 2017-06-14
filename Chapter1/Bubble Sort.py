def bubbleSort(a):
    n = len(a)

    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

a = [2,5,4,8,10,3,15]
bubbleSort(a)
print("Sorted array is:")
for i in range (len(a)):
    print("%d" %a[i])
                
