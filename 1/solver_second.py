import re

file1 = open('data.txt', 'r')
Lines = file1.readlines()

numbersDict = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
  "zero": 0,
}
selfNumbersDict = {
  "1": 1,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "0": 0,
}

numbersLookupDict = numbersDict | selfNumbersDict

for key in numbersDict:
  numbersLookupDict[key[::-1]] = numbersLookupDict[key]

numbersStr = "|".join(numbersDict.keys())
numRegex = "(\\d|" + numbersStr + ")"
revNumRegex = "(\\d|" + numbersStr[::-1] + ")"
sum = 0
for line in Lines:
  firstDigit = numbersLookupDict[re.search(numRegex, line).group()]
  secondDigit = numbersLookupDict[re.search(revNumRegex, line[::-1]).group()]
  number = int(str(firstDigit) + "" + str(secondDigit))
  sum += number
print(sum)
