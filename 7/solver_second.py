cards =   ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
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

def jokersplit(hand):
  jokers = 0
  non_jokers = ""
  for card in hand:
    if card == "J":
      jokers += 1
    else:
      non_jokers += card
  return [jokers, non_jokers]

def fiveofakind(hand):
  if len(hand) != 5:
    return False
  firstcard = hand[0]
  for card in hand[1:]:
    if not card == firstcard:
      return False
  return True

def fourofakind(hand):
  if len(hand) < 4:
    return False
  occurencedict = buildoccurencedict(hand)
  for card in occurencedict:
    if occurencedict[card] == 4:
      return True
  return False

def fullhouse(hand):
  if len(hand) != 5:
    return False
  occurencedict = buildoccurencedict(hand)
  occkeys = list(occurencedict.keys())
  if not len(occkeys) == 2:
    return False
  amounts = [2,3]
  amounts.remove(occurencedict[occkeys[0]])
  return True if occurencedict[occkeys[1]] == amounts[0] else False

def threeofakind(hand):
  if len(hand) < 3:
    return False
  occurencedict = buildoccurencedict(hand)
  occkeys = list(occurencedict.keys())
  for occkey in occurencedict:
    if occurencedict[occkey] == 3:
      return True

def twopair(hand):
  if len(hand) < 4:
    return False
  occurencedict = buildoccurencedict(hand)
  numTwos = 0
  for occkey in occurencedict:
    if occurencedict[occkey] == 2:
      numTwos += 1
  return numTwos == 2

def onepair(hand):
  if len(hand) < 2:
    return False
  occurencedict = buildoccurencedict(hand)
  onepairalready = False
  for occkey in occurencedict:
    if occurencedict[occkey] == 2:
      if onepairalready:
        return False
      onepairalready = True
  return onepairalready

def highcard(hand):
  occurencedict = buildoccurencedict(hand)
  return True if len(occurencedict.keys()) == len(hand) else False

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

def handtype(jokers, non_jokers):
  if fiveofakind(non_jokers):
    return handtypes["fiveofakind"]
  if fourofakind(non_jokers):
    return handtypes["fourofakind"] + jokers
  if fullhouse(non_jokers):
    return handtypes["fullhouse"]
  if threeofakind(non_jokers):
    if jokers == 0:
      return handtypes["threeofakind"]
    else:
      return handtypes["threeofakind"] + 1 + jokers
  if twopair(non_jokers):
    if jokers == 0:
      return handtypes["twopair"]
    else:
      return handtypes["fullhouse"]
  if onepair(non_jokers):
    if jokers == 0:
      return handtypes["onepair"]
    elif jokers == 1:
      return handtypes["threeofakind"]
    elif jokers == 2:
      return handtypes["fourofakind"]
    else:
      return handtypes["fiveofakind"]
  if highcard(non_jokers):
    if jokers == 0:
      return handtypes["highcard"]
    elif jokers == 1:
      return handtypes["onepair"]
    elif jokers == 2:
      return handtypes["threeofakind"]
    elif jokers == 3:
      return handtypes["fourofakind"]
    else:
      return handtypes["fiveofakind"]
  print("no handtype:")
  print(jokers, non_jokers)

def main():
  data_file = open('data.txt', 'r')
  lines = data_file.read().splitlines()
  hands = {}
  for line in lines:
    hand, bet = line.split()
    jokers, non_jokers = jokersplit(hand)
    # print(jokers, non_jokers)
    thishandtype = handtype(jokers, non_jokers)
    print(thishandtype, hand)
    if thishandtype not in hands:
      hands[thishandtype] = []
    hands[thishandtype].append([hand, bet])
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