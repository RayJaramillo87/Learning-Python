import random, sys
numberOfStreaks = 0

print('How many experiments should we run?')

try:
    numberofExperiments = int(input())
except ValueError:
    print('Invalid Entry')

try:
    for experimentNumber in range(numberofExperiments):
        # Code that creates a list of 100 'heads' or 'tails' values.
        results = []
        for coinFlips in range(100):
            coinFlip = random.randint(0,1)
            if coinFlip == 0:
                results.append('H')
                #print('Heads!')
            elif coinFlip == 1:
                results.append('T')
                #print('Tails!')
            #print(results)

        # Code that checks if there is a streak of 6 heads or tails in a row.
        match = 0
        for i in range(len(results)):
            if results[i] == results[i - 1]:
                match += 1
                if match == 80:
                    numberOfStreaks += 1
                    match = 0
            elif results[i] == results[i -1]:
                match = 0
except NameError:
    sys.exit()

print('Chance of streak: %s%%' % "{:.3}".format((numberOfStreaks / numberofExperiments)))
print('Total Streaks: ' + str(numberOfStreaks))