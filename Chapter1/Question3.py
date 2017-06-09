#Q3: Write a method to replace all spaces in string with %20


def urlifyString(str):
    res = ''
    start = False
    str = str.strip() # Removes white space from the beginning and end of the string
    for char in str:
        if(char == ' '):
            res += '%20'
        else: res += char
    return res
 
print (urlifyString("       Mr John Smith           "))
    
