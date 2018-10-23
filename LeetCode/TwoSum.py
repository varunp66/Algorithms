''' This is a brute force method
The loop the take the input elements an array 'a' and the target value.
The first loop will run through all the elements in the array from the
first element and then compare it with the next elements and it will check whether
we are getting the target value.
The second loop will run through all the elements ignoring the all previous
elements.

'''
a= [-2, 1,2,4,7,11]
target = 13

def two_sum(a,target):
    for i in range(len(a)-1):
        for j in range(i+1, len(A)):
            if a[i] + a[j] == target:
                print(a[i], a[j])
                return True
    return False

print(two_sum(a, target))
