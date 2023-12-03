data_file = open('data.txt', 'r')
lines = data_file.readlines()
first_last_line = "".ljust(140, ".")

lines.insert(0, first_last_line)
lines.append(first_last_line)

digits = {"0","1","2","3","4","5","6","7","8","9"}
gear = "*"
gears = {}

def main():
  sum = 0
  idx = 1
  while idx < len(lines)-1:
    gears[idx] = {}
    idx += 1
  idx = 1
  while idx < len(lines)-1:
    number = ""
    for cdx, c in enumerate(lines[idx]):
      if c in digits:
        number += c
      elif len(number) > 0:
        look_around([lines[idx-1],lines[idx],lines[idx+1]], cdx-len(number), cdx, idx)
        number = ""
    if len(number) > 0:
      look_around([lines[idx-1],lines[idx],lines[idx+1]], len(lines[0])-1-len(number), len(lines[0])-1, idx)
      number = ""
    idx += 1
  for ydx in gears:
    for xdx in gears[ydx]:
      if len(gears[ydx][xdx]) == 2:
        sum += gears[ydx][xdx][0]*gears[ydx][xdx][1]
  print(sum)

def look_around(lines, number_start_index, number_end_index, y_index):
  x_coord = max(0, number_start_index-1)
  y_coord = 0

  the_number = int(lines[1][number_start_index:number_end_index])

  if not number_start_index == 0 and lines[1][number_start_index-1] == gear:
    if (number_start_index-1) not in gears[y_index]:
      gears[y_index][number_start_index-1] = []
    gears[y_index][number_start_index-1].append(the_number)
  if not number_end_index == len(lines[0])-1 and lines[1][number_end_index] == gear:
    if number_end_index not in gears[y_index]:
      gears[y_index][number_end_index] = []
    gears[y_index][number_end_index].append(the_number)
  while True:
    if lines[y_coord][x_coord] == gear:
      if x_coord not in gears[y_index-1+y_coord]:
        gears[y_index-1+y_coord][x_coord] = []
      gears[y_index-1+y_coord][x_coord].append(the_number)
    x_coord += 1
    if x_coord == len(lines[0]) or x_coord == number_end_index+1:
      if (y_coord == 2):
        return
      y_coord = 2
      x_coord = max(0, number_start_index-1)
    
    

if __name__ == "__main__":
    main()