def main():
  data_file = open('data.txt', 'r')
  lines = data_file.read().splitlines()
  leftsrights = []
  mymap = {}
  for line in lines:
    if len(leftsrights) == 0:
      for char in line:
        if char == "L":
          leftsrights.append(0)
        else:
          leftsrights.append(1)
      continue
    if line == "":
      continue
    orig, dests = line.split(" = (")
    destleft, destright = dests[:-1].split(", ")
    mymap[orig] = [destleft, destright]
  steps = 0
  idx = 0
  start = "AAA"
  cur = start
  goal = "ZZZ"
  while True:
    cur = mymap[cur][leftsrights[idx]]
    steps += 1
    if cur == goal:
      break
    idx += 1
    if idx >= len(leftsrights):
      idx = 0
  print(steps)

if __name__ == "__main__":
    main()