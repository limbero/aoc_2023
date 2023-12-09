def main():
  data_file = open('data.txt', 'r')
  lines = data_file.read().splitlines()
  prediction_sum = 0
  for line in lines:
    sequence = list(map(lambda x: int(x), line.split()))
    thisseq = sequence.copy()
    seqs = [sequence]
    while True:
      diffs = []
      idx = 1
      while idx < len(thisseq):
        diffs.append(thisseq[idx]-thisseq[idx-1])
        idx += 1
      allZeroes = True
      for diff in diffs:
        if diff != 0:
          allZeroes = False
      if allZeroes:
        break
      seqs.append(diffs)
      thisseq = diffs.copy()
    idx = len(seqs) - 2
    while idx >= 0:
      nextpred = seqs[idx][0] - seqs[idx+1][0]
      seqs[idx].insert(0, nextpred)
      idx -= 1
    prediction_sum += seqs[0][0]
    # print(seqs)
    # break
  print(prediction_sum)

if __name__ == "__main__":
    main()