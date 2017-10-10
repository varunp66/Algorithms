'''def linearSearch(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1

arr = [1,5,3,8,12,75]
x=12
linearSearch(arr,x)
print(arr[i])        '''


list = [4,1,2,5,3]  #set up array
search = int(input("Enter search number: "))    # ask for a number
for i in range(0,len(list)): # repeat for each item in list
  if search==list[i]: #if item at position i is search time
    print(str(search) + " found at position " + str(i)) #report find
