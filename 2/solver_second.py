data_file = open('data.txt', 'r')
lines = data_file.readlines()

sum = 0
for line in lines:
  minimums = {
    "red": 0,
    "green": 0,
    "blue": 0,
  }
  pieces = line.strip().split(": ")
  id = pieces[0].split(" ")[1]
  revealed_sets = pieces[1].split("; ")
  for set in revealed_sets:
    reavealed_cubes = set.split(", ")
    for cube in reavealed_cubes:
      num, color = cube.split(" ")
      if int(num) > minimums[color]:
        minimums[color] = int(num)
  sum += minimums["red"] * minimums["green"] * minimums["blue"]

print(sum)