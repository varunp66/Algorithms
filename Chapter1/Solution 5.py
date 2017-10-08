
# Given 2 strings, write a function to check if they
# are only one edit or zero edits away from each other

# pale, ple -> True
# pale, pales -> True
# pale, bale -> True
# pale, bae -> False
# pale, pale -> True

#Time Complexity = O(n)
#Replace, Add, Delete

def isOneEditAway(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    if str1 == str2:
        return True
    elif len(str1) == len(str2):
        return isReplace(str1, str2)
    elif len(str2) == len(str1) + 1:
        return isDelete(str1, str2)
    elif len(str2) == len(str1) - 1:
        return isAdd(str1, str2)
    else: return False

def isReplace(str1, str2):
    i = 0
    for a, b in zip(str1, str2):
        if b != a:
            str2[i] = a
            if ''.join(str2) == ''.join(str1):
                return True
            else: return False
        i += 1

def isAdd(str1, str2):
    i = 0 #str1 index
    j = 0 #str2 index
    while i < len(str2):
        if str1[i] != str2[j]:
            if i != j:
                return False
            else: i += 1
        else:
            i += 1
            j += 1
    return True

def isDelete(str1, str2):
    i = 0
    for char in str2:
        if i == len(str1):
            str2.remove(char)
            return True
        elif char != str1[i]:
                str2.remove(char)
                if str2 == str1:
                    return True
                else: return False
        i += 1

print (isOneEditAway("pale", "pale"))
