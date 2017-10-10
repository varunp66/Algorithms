'''Implement a method to perform basic string compression using
   the counts of repeated characters method.'''


def string_compression(input):
  
  if len(input) == 0:
    return ""
  
  counter = 1
  output = ''
  
  for i in range(1,len(input)):
  
    if input[i] == input[i-1]:
      counter += 1
  
    else:
      output += input[i-1] + str(counter)
      counter = 1
  
  output += input[-1] + str(counter)
  
  return output
  
print (string_compression("aaaacbbbtttbbccc"))


