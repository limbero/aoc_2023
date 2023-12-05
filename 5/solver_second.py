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
  maps.reverse()
  maps = list(map(mysort, maps))
  # print(maps)
  # print(map_backwards(0, maps))
  corr_loc = 52510809
  loc = 0
  done = False
  # for loc_lower, _, range_length in maps[0]:
  #   idx = loc_lower
  #   while idx < loc_lower + range_length:
  #     seed = map_backwards(idx, maps)
  #     print(str(idx) + " comes from " + str(seed))
  #     idx += 1
  # return

  while not done:
    print("{:.2f}".format(loc/corr_loc) + "% done", end='\r')
    seed = map_backwards(loc, maps)
    # print(str(loc) + " comes from " + str(seed))
    # print(seed)
    tidx = 0
    while tidx < len(seeds):
      lower_bound = seeds[tidx]
      upper_bound = seeds[tidx] + seeds[tidx+1]
      if seed >= lower_bound and seed < upper_bound:
        done = True
        print(loc)
      tidx += 2
    loc += 1
  print()

def mysort(y):
  y.sort(key=lambda x: x[0])
  return y
  
def map_backwards(loc, maps):
  thing = loc
  for curmap in maps:
    # print("step: " + str(counter))
    # counter += 1
    been_mapped = False
    # print(thing)
    for dest_range, source_range, range_length in curmap:
      # print(dest_range, source_range, range_length)
      if been_mapped:
        break
      diff = source_range - dest_range
      if thing >= dest_range and thing < (dest_range + range_length):
        # print(thing)
        been_mapped = True
        thing = thing + diff
  # print(thing)
  # print(maps)
  # print(min(things))
  return thing
  
def map_all_the_way(thing, maps):
  counter = 1
  things = [thing]
  for curmap in maps:
    # print("step: " + str(counter))
    counter += 1
    been_mapped = list(map(lambda _: False, things))
    for dest_range, source_range, range_length in curmap:
      # print(dest_range, source_range, range_length)
      diff = dest_range - source_range
      for idx, thing in enumerate(things):
        if not been_mapped[idx] and thing >= source_range and thing < (source_range + range_length):
          been_mapped[idx] = True
          things[idx] = thing + diff
  # print(maps)
  # print(min(things))
  return things[0]
      
if __name__ == "__main__":
    main()