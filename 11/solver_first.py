def main():
  data_file = open('data.txt', 'r')
  lines = data_file.read().splitlines()
  
  ydx = 0
  empty_rows = []
  while ydx < len(lines):
    alldots = True
    xdx = 0
    while xdx < len(lines[0]):
      if lines[ydx][xdx] != ".":
        alldots = False
        break
      xdx += 1
    if alldots:
      empty_rows.insert(0, ydx)
    ydx += 1

  xdx = 0
  empty_cols = []
  while xdx < len(lines[0]):
    alldots = True
    ydx = 0
    while ydx < len(lines):
      if lines[ydx][xdx] != ".":
        alldots = False
        break
      ydx += 1
    if alldots:
      empty_cols.insert(0, xdx)
    xdx += 1
  
  for col in empty_cols:
    for idx, line in enumerate(lines):
      lines[idx] = line[:col] + "." + line[col:]
  
  for row in empty_rows:
    lines.insert(row, lines[row])

  galaxies = []
  xdx = 0
  while xdx < len(lines[0]):
    ydx = 0
    while ydx < len(lines):
      if lines[ydx][xdx] != ".":
        galaxies.append({"x": xdx, "y": ydx})
      ydx += 1
    xdx += 1
  
  distances = 0
  while len(galaxies) > 0:
    this_galaxy = galaxies[0]
    galaxies.remove(this_galaxy)
    for other_galaxy in galaxies:
      distance = abs(this_galaxy["x"] - other_galaxy["x"])
      distance += abs(this_galaxy["y"] - other_galaxy["y"])
      distances += distance
  print(distances)

if __name__ == "__main__":
    main()