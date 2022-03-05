import os
def clearConsole(): # we stan a good clear command
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command) 
chromatic = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
scaleStorage = []
majorPattern = [2, 2, 1, 2, 2, 2, 1]
minorPattern = [2, 1, 2, 2, 1, 2, 2]
harminorPattern = [2, 1, 2, 2, 1, 3, 1]
melminorPattern = [2, 1, 2, 2, 2, 2, 1]
dorianPattern = [2, 1, 2, 2, 2, 1, 2]
mixPattern = [2, 2, 1, 2, 2, 1, 2]
minPentPattern = [3, 2, 2, 3, 2]
majPentPattern = [2, 2, 3, 2, 3]
blues = [3, 2, 1, 1, 3, 2]
while True:
  # I hate the formatting of this text but what am i gonna do about it
  scale = input("What scale would you like?\n Syntax: keyname (if a sharp or a flat please also put it's equivalent)\n [e.g. F#/Gb]\n then Major or Minor\n For other key types (e.g. harmonic minor) please type it as one word\n with maj or min shortened e.g. HarmonicMin\n\n")
  scaleName = scale.split()
  clearConsole()
  # pattern determiner
  # can't be arsed to optimise
  if "Major" in scaleName:
    pattern = majorPattern
  elif "Minor" in scaleName:
    pattern = minorPattern
  elif "HarmonicMin" in scaleName:
    pattern = harminorPattern
  elif "MelodicMin" in scaleName:
    pattern = melminorPattern
  elif "Dorian" in scaleName:
    pattern = dorianPattern
  elif "Mixolydian" in scaleName:
    pattern = mixPattern
  elif "PentatonicMin" in scaleName:
    pattern = minPentPattern
  elif "PentatonicMaj" in scaleName:
    pattern = majPentPattern
  elif "Blues" in scaleName:
    pattern = blues
  else:
    input("Invalid, please check your syntax.\n(ENTER to continue.)")
    clearConsole()
    continue
  # the bit that does the maths
  runningTotal = chromatic.index(scaleName[0])
  print(chromatic[runningTotal])
  scaleStorage.append(chromatic[runningTotal])
  for i in range(len(pattern)):
    runningTotal += pattern[i]
    checkTotal = runningTotal - pattern[i]
    try:
      print(chromatic[runningTotal])
      scaleStorage.append(chromatic[runningTotal])
    except:
      if pattern[i] == 2:
        if chromatic[checkTotal] == "A#/Bb":
          runningTotal = 0
          print(chromatic[runningTotal])
          scaleStorage.append(chromatic[runningTotal])
        else:
          runningTotal = 1
          print(chromatic[runningTotal])
          scaleStorage.append(chromatic[runningTotal])
      elif pattern[i] == 3:
        if chromatic[checkTotal] == "A":
          runningTotal = 0
          print(chromatic[runningTotal])
          scaleStorage.append(chromatic[runningTotal])
        elif chromatic[checkTotal] == "A#/Bb":
          runningTotal = 1
          print(chromatic[runningTotal])
          scaleStorage.append(chromatic[runningTotal])
        else:
          runningTotal = 2
          print(chromatic[runningTotal])
          scaleStorage.append(chromatic[runningTotal])
      else:
        runningTotal = 0
        print(chromatic[runningTotal])
        scaleStorage.append(chromatic[runningTotal])
  # progression
  if "Major" in scaleName:
    print("Common progression (* area is the circular):")
    print("* " + scaleStorage[2] + " → " + scaleStorage[5] + " → [" + scaleStorage[1] + " or " + scaleStorage[3] + "] → [" + scaleStorage[4] + " or " + scaleStorage[6] + "°] * → " + scaleStorage[0] + " → ANY")
    input("Press ENTER to continue")
    clearConsole()
  elif "Minor" in scaleName:
    print("Common progression (* area is the circular):")
    print("* " + scaleStorage[6] + " → " + scaleStorage[2] + " → " + scaleStorage[5] + " → [" + scaleStorage[1] + " or " + scaleStorage[3] + "] * → [" + scaleStorage[4] + " or " + scaleStorage[6] + "°] → " + scaleStorage[0] + " → ANY")
    input("Press ENTER to continue")
    clearConsole()
  else: 
    input("Press ENTER to continue")
    clearConsole()
    continue