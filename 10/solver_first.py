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
  if sentineled_map[sloc["y"]-1][sloc["x"]] in ["|", "F", "7"]:   # north
    cury -= 1
    camefrom = "S"
  elif sentineled_map[sloc["y"]][sloc["x"]+1] in ["|", "F", "7"]: # east
    curx += 1
    camefrom = "W"
  elif sentineled_map[sloc["y"]+1][sloc["x"]] in ["|", "F", "7"]: # south
    cury += 1
    camefrom = "N"
  elif sentineled_map[sloc["y"]][sloc["x"]-1] in ["|", "F", "7"]: # west
    curx -= 1
    camefrom = "E"
  dist = 1
  curchar = sentineled_map[cury][curx]
  while curchar != "S":
    nextdir = findnext(curchar, camefrom)
    camefrom = opposite[nextdir]
    nextlocdiff = dirs[nextdir]

    curx += nextlocdiff["x"]
    cury += nextlocdiff["y"]
    curchar = sentineled_map[cury][curx]
    dist += 1
  print(dist/2)

if __name__ == "__main__":
    main()