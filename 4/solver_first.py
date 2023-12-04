def main():
  data_file = open('data.txt', 'r')
  lines = data_file.readlines()
  sum = 0
  for line in lines:
    score = 0
    winning_numbers, my_numbers = line.strip().split(": ")[1].split(" | ")
    winning_numbers = winning_numbers.strip().replace("  ", " ").split(" ")
    my_numbers = my_numbers.strip().replace("  ", " ").split(" ")
    for my_number in my_numbers:
      if not my_number.isnumeric():
        print(my_numbers)
      if my_number in winning_numbers:
        score += 1
    if score > 0:
      sum += 2 ** (score-1)
  print(sum)

if __name__ == "__main__":
  main()