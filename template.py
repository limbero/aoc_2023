def main():
  data_file = open('data.txt', 'r')
  lines = data_file.read().splitlines()
  for line in lines:
    print(line)

if __name__ == "__main__":
    main()