import re

file1 = open('data.txt', 'r')
Lines = file1.readlines()
 
numRegex = r"\d"
sum = 0
for line in Lines:
  firstDigit = re.search(numRegex, line).group()
  secondDigit = re.search(numRegex, line[::-1]).group()
  number = int(firstDigit + "" + secondDigit)
  sum += number
print(sum)
