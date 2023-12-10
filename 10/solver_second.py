def add_sentinel_border(lines, mychar):
  newlines = lines.copy()
  for idx, line in enumerate(newlines):
    newlines[idx] = mychar + line + mychar
  borderline = mychar * len(newlines[0])
  newlines.insert(0, borderline)
  newlines.append(borderline)
  return newlines

dirs = {
  "N": { "x": 0,  "y": -1 },
  "E": { "x": 1,  "y": 0  },
  "S": { "x": 0,  "y": 1  },
  "W": { "x": -1, "y": 0  },
}

opposite = {
  "N": "S",
  "E": "W",
  "S": "N",
  "W": "E",
}

def findnext(curchar, camefrom):
  if camefrom == "N":
    if curchar == "|":
      return "S"
    elif curchar == "L":
      return "E"
    elif curchar == "J":
      return "W"
  elif camefrom == "E":
    if curchar == "-":
      return "W"
    elif curchar == "L":
      return "N"
    elif curchar == "F":
      return "S"
  elif camefrom == "S":
    if curchar == "|":
      return "N"
    elif curchar == "7":
      return "W"
    elif curchar == "F":
      return "E"
  elif camefrom == "W":
    if curchar == "-":
      return "E"
    elif curchar == "J":
      return "N"
    elif curchar == "7":
      return "S"

def main():
  data_file = open('data.txt', 'r')
  lines = data_file.read().splitlines()
  sentineled_map = add_sentinel_border(lines, ".")
  sloc = None
  for ydx, line in enumerate(sentineled_map):
    for xdx, char in enumerate(line):
      if char == "S":
        sloc = { "x": xdx, "y": ydx }

  curx = sloc["x"]
  cury = sloc["y"]
  camefrom = None
  have_set = False
  sdirs = []
  if sentineled_map[sloc["y"]-1][sloc["x"]] in ["|", "F", "7"]:   # north
    sdirs.append("N")
    cury -= 1
    camefrom = "S"
    have_set = True
  if sentineled_map[sloc["y"]][sloc["x"]+1] in ["-", "J", "7"]: # east
    sdirs.append("E")
    if not have_set:
      curx += 1
      camefrom = "W"
  if sentineled_map[sloc["y"]+1][sloc["x"]] in ["|", "J", "L"]: # south
    sdirs.append("S")
    if not have_set:
      cury += 1
      camefrom = "N"
  if sentineled_map[sloc["y"]][sloc["x"]-1] in ["-", "F", "L"]: # west
    sdirs.append("W")
    if not have_set:
      curx -= 1
      camefrom = "E"

  line_locs = [[curx, cury]]
  dist = 1
  curchar = sentineled_map[cury][curx]
  while curchar != "S":
    nextdir = findnext(curchar, camefrom)
    camefrom = opposite[nextdir]
    nextlocdiff = dirs[nextdir]

    curx += nextlocdiff["x"]
    cury += nextlocdiff["y"]
    line_locs.append([curx, cury])
    curchar = sentineled_map[cury][curx]
    dist += 1
  
  sdirs.sort()
  sdirs = "".join(sdirs)
  s_actual_char = "S"
  if sdirs == "NS":
    s_actual_char = "|"
  elif sdirs == "NW":
    s_actual_char = "J"
  elif sdirs == "EN":
    s_actual_char = "L"
  elif sdirs == "ES":
    s_actual_char = "F"
  elif sdirs == "EW":
    s_actual_char = "-"
  elif sdirs == "SW":
    s_actual_char = "7"

  sentineled_map[sloc["y"]] = sentineled_map[sloc["y"]][:sloc["x"]] + s_actual_char + sentineled_map[sloc["y"]][sloc["x"] + 1:]

  squares_inside = 0
  for ydx, line in enumerate(sentineled_map):
    is_inside = False
    on_the_line = False
    line_start_char = None
    for xdx, char in enumerate(line):
      # if ydx == 75:
        # print(is_inside, char, xdx, ydx, on_the_line, line_start_char)
      if [xdx, ydx] in line_locs:
        if char == "|":
          is_inside = not is_inside
          # if ydx == 75:
          #   print("cross")
        elif char in ["F", "L"]:
          on_the_line = True
          line_start_char = char
        elif on_the_line:
          if char == "-":
            continue
          elif char == "7":
            on_the_line = False
            if line_start_char == "L":
              is_inside = not is_inside
              # if ydx == 75:
              #   print("cross")
          elif char == "J":
            on_the_line = False
            if line_start_char == "F":
              is_inside = not is_inside
              # if ydx == 75:
              #   print("cross")
          line_start_char = None
      elif is_inside:
        # print(char)
        squares_inside += 1

        # if ydx == 75:
        #   print(is_inside, char, xdx, ydx)
        # if xdx == (len(line)-1):
        #   print("hmm")
        #   print(xdx,ydx)
  print(squares_inside)
      
        

# | is a vertical pipe connecting north and south. X
# - is a horizontal pipe connecting east and west. X
# L is a 90-degree bend connecting north and east. X
# J is a 90-degree bend connecting north and west. X
# 7 is a 90-degree bend connecting south and west. X
# F is a 90-degree bend connecting south and east. X
# . is ground; there is no pipe in this tile.
# S is the starting position

if __name__ == "__main__":
    main()