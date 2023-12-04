def main():
  data_file = open('data.txt', 'r')
  lines = data_file.readlines()
  # sum = 0
  static_list = []
  for line in lines:
    line_no = int(line.strip().split(": ")[0][5:])
    winning_numbers, my_numbers = line.strip().split(": ")[1].split(" | ")
    winning_numbers = winning_numbers.strip().replace("  ", " ").split(" ")
    my_numbers = my_numbers.strip().replace("  ", " ").split(" ")
    static_list.append([line_no, winning_numbers, my_numbers])
  extending_list = static_list[:]
  for idx, numbers in enumerate(extending_list):
    line_no, winning_numbers, my_numbers = numbers
    score = 0
    for my_number in my_numbers:
      if my_number in winning_numbers:
        score += 1
    if score > 0:
      start_index = line_no
      end_index = min(line_no + score, len(static_list))
      # print("start_index: " + str(start_index) + ", end_index: " + str(end_index))
      extending_list.extend(static_list[start_index:end_index])
  print(len(extending_list))

if __name__ == "__main__":
  main()