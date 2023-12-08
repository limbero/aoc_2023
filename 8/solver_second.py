from math import lcm

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
  starts = list(filter(lambda txt: txt[2] == "A", list(mymap.keys())))
  math_way(mymap, leftsrights, starts)

def math_way(mymap, leftsrights, starts):
  dists_to_zs = []
  for start in starts:
    steps = 0
    idx = 0
    cur = start
    while True:
      cur = mymap[cur][leftsrights[idx]]
      steps += 1
      if cur[2] == "Z":
        dists_to_zs.append(steps)
        break
      idx += 1
      if idx >= len(leftsrights):
        idx = 0
  print(lcm(*dists_to_zs))

if __name__ == "__main__":
    main()