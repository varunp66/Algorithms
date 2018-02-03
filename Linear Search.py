# Linear Search

list = [4,1,2,5,3,7,9, 12, 6]  #set up array

search = int(input("Enter search number: "))    # Take input from User

for i in range(0,len(list)): # repeat for each item in list
  if search==list[i]: #if item at position i is search time
    print(str(search) + " found at position " + str(i)) #report find
