data_file = open('data.txt', 'r')
lines = data_file.readlines()
first_last_line = "".ljust(140, ".")

lines.insert(0, first_last_line)
lines.append(first_last_line)

digits = {"0","1","2","3","4","5","6","7","8","9"}
non_symbols = digits | {".", "\n"}

def main():
  sum = 0
  idx = 1
  while idx < len(lines)-1:
    number = ""
    for cdx, c in enumerate(lines[idx]):
      if c in digits:
        number += c
      elif len(number) > 0:
        tempnum = int(number)
        if look_around([lines[idx-1],lines[idx],lines[idx+1]], cdx-len(number), cdx):
          sum += tempnum
        number = ""
    if len(number) > 0:
      tempnum = int(number)
      if look_around([lines[idx-1],lines[idx],lines[idx+1]], len(lines[0])-1-len(number), len(lines[0])-1):
        sum += tempnum
      number = ""
    idx += 1
  print(sum)

def look_around(lines, number_start_index, number_end_index):
  x_coord = max(0, number_start_index-1)
  y_coord = 0

  the_number = lines[1][number_start_index:number_end_index]

  if not number_start_index == 0 and lines[1][number_start_index-1] not in non_symbols:
    if the_number == "101":
      print("före")
    return True
  if not number_end_index == len(lines[0])-1 and lines[1][number_end_index] not in non_symbols:
    if the_number == "101":
      print("efter")
    return True
  while True:
    if lines[y_coord][x_coord] not in non_symbols:
      if the_number == "101":
        if y_coord == 0:
          print("över")
          print(len(lines[y_coord]))
          print(lines[y_coord][x_coord])
          print(str(x_coord) + "," + str(y_coord))
        else:
          print("under")
          print(str(x_coord) + "," + str(y_coord))
      return True
    x_coord += 1
    if x_coord == len(lines[0]) or x_coord == number_end_index+1:
      if (y_coord == 2):
        return False
      y_coord = 2
      x_coord = max(0, number_start_index-1)
    
    

if __name__ == "__main__":
    main()