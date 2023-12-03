data_file = open('data.txt', 'r')
lines = data_file.readlines()

limits = {
  "red": 12,
  "green": 13,
  "blue": 14,
}
sum = 0
for line in lines:
  valid_line = True
  pieces = line.strip().split(": ")
  id = pieces[0].split(" ")[1]
  revealed_sets = pieces[1].split("; ")
  for set in revealed_sets:
    reavealed_cubes = set.split(", ")
    for cube in reavealed_cubes:
      num, color = cube.split(" ")
      if int(num) > limits[color]:
        valid_line = False
        break
    if not valid_line:
      break
  if valid_line:
    sum += int(id)

print(sum)