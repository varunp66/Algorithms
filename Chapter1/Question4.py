'''Q4: Given a string writhing a function to chack if it is a
   permutaion of a Palindrome.'''

#Permutation means re-arrangement.
#Palindrome is which is same from front and back.

import string

def isPermOfPalindrome(str):
    d = dict.fromkeys(string.ascii_lowercase, False)  # We have use dictionary here
    count = 0
    for char in str:
        if(ord(char) > 96 and ord(char) < 123):     # We are taking only lower case ASCII values
            d[char] = not d[char]   #We are toggleing the value
    for key in d:
        if d[key] is True:
            count += 1
            if count > 1:
                return False
    return True

print (isPermOfPalindrome("aa bb cc eee"))

# We can change the above string and can test different conditions.
