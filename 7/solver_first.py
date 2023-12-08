cards =   ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
letters = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n"]

# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456

def buildoccurencedict(hand):
  occurencedict = {}
  for card in hand:
    if card in occurencedict:
      occurencedict[card] += 1
    else:
      occurencedict[card] = 1
  return occurencedict

def fiveofakind(hand):
  firstcard = hand[0]
  for card in hand[1:]:
    if not card == firstcard:
      return False
  return True

def fourofakind(hand):
  occurencedict = buildoccurencedict(hand)
  for card in occurencedict:
    if occurencedict[card] == 4:
      return True
  return False

def fullhouse(hand):
  occurencedict = buildoccurencedict(hand)
  occkeys = list(occurencedict.keys())
  if not len(occkeys) == 2:
    return False
  amounts = [2,3]
  amounts.remove(occurencedict[occkeys[0]])
  return True if occurencedict[occkeys[1]] == amounts[0] else False

def threeofakind(hand):
  occurencedict = buildoccurencedict(hand)
  occkeys = list(occurencedict.keys())
  if not len(occkeys) == 3:
    return False
  for occkey in occurencedict:
    if occurencedict[occkey] == 2:
      return False
  amounts = [1,1,3]
  amounts.remove(occurencedict[occkeys[0]])
  amounts.remove(occurencedict[occkeys[1]])
  return True if occurencedict[occkeys[2]] == amounts[0] else False

def twopair(hand):
  occurencedict = buildoccurencedict(hand)
  occkeys = list(occurencedict.keys())
  if not len(occkeys) == 3:
    return False
  for occkey in occurencedict:
    if occurencedict[occkey] == 3:
      return False
  amounts = [2,2,1]
  amounts.remove(occurencedict[occkeys[0]])
  amounts.remove(occurencedict[occkeys[1]])
  return True if occurencedict[occkeys[2]] == amounts[0] else False

def onepair(hand):
  occurencedict = buildoccurencedict(hand)
  occkeys = list(occurencedict.keys())
  if not len(occkeys) == 4:
    return False
  amounts = [2,1,1,1]
  amounts.remove(occurencedict[occkeys[0]])
  amounts.remove(occurencedict[occkeys[1]])
  amounts.remove(occurencedict[occkeys[2]])
  return True if occurencedict[occkeys[3]] == amounts[0] else False

def highcard(hand):
  occurencedict = buildoccurencedict(hand)
  return True if len(occurencedict.keys()) == 5 else False

def sortablehand(hand):
  newstr = ""
  for card in hand:
    newstr += letters[cards.index(card)]
  return newstr

def sortablehandandbet(handandbet):
  return [sortablehand(handandbet[0]), handandbet[1]]

handtypes = {
  "highcard": 0,
  "onepair": 1,
  "twopair": 2,
  "threeofakind": 3,
  "fullhouse": 4,
  "fourofakind": 5,
  "fiveofakind": 6,
}

def handtype(hand):
  if fiveofakind(hand):
    return handtypes["fiveofakind"]
  if fourofakind(hand):
    return handtypes["fourofakind"]
  if fullhouse(hand):
    return handtypes["fullhouse"]
  if threeofakind(hand):
    return handtypes["threeofakind"]
  if twopair(hand):
    return handtypes["twopair"]
  if onepair(hand):
    return handtypes["onepair"]
  if highcard(hand):
    return handtypes["highcard"]

def main():
  data_file = open('data.txt', 'r')
  lines = data_file.read().splitlines()
  hands = {}
  for line in lines:
    hand, bet = line.split()
    thishandtype = handtype(hand)
    if thishandtype not in hands:
      hands[handtype(hand)] = []
    hands[handtype(hand)].append([hand, bet])
  listoflists = []
  idx = 0
  while idx <= 6:
    if idx in hands:
      listoflists.append(hands[idx])
    idx += 1
  sortedlistoflists = []
  for handslist in listoflists:
    sortedlistoflists.append(sorted(handslist, key=sortablehandandbet))
  sortedhands = []
  for handslist in sortedlistoflists:
    for hand in handslist:
      sortedhands.append(hand)
  sum = 0
  for idx, hand in enumerate(sortedhands):
    sum += int(hand[1]) * (idx + 1)
  print(sum)

if __name__ == "__main__":
    main()