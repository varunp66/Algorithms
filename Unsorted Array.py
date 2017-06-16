'''def findElement(arr,n,key):
    for i in range(n):
        if (arr[i] == key):
            return i
    return -1

arr = [12,23,1,45,3,32]
key = 40
n = len(arr)

index = findElement(arr, n , key)
if index != -1:
    print("element found at position:" + str(index +1))
else:
    print("element not found")'''
    
def insert(arr, element):
    arr.append(element)
 
# declaring array and key to insert 
arr = [12, 16, 20, 40, 50, 70]
key = 26
  
# array before inserting an element
print ("Before Inserting: ")
print (arr)
  
# array after Inserting element 
insert(arr, key)
print("After Inserting: ")
print (arr)
