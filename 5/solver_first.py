def main():
  data_file = open('data.txt', 'r')
  lines = data_file.read().splitlines()
  seeds = []
  maps = []
  thismap = None
  for idx, line in enumerate(lines):
    if idx == 0:
      seeds = list(map(int, line.split(": ")[1].split()))
    elif line == "":
      continue
    elif ":" in line:
      if thismap:
        maps.append(thismap)
      thismap = []
    else:
      thismap.append(list(map(int, line.split())))
  maps.append(thismap)
  
  things = seeds[:]
  for curmap in maps:
    been_mapped = list(map(lambda _: False, things))
    for dest_range, source_range, range_length in curmap:
      # print(dest_range, source_range, range_length)
      diff = dest_range - source_range
      for idx, thing in enumerate(things):
        if not been_mapped[idx] and thing >= source_range and thing < (source_range + range_length):
          been_mapped[idx] = True
          things[idx] = thing + diff
  # print(maps)
  print(min(things))
      
if __name__ == "__main__":
    main()