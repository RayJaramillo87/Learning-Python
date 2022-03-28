import random,sys
from tkinter import Y
import matplotlib.pyplot as plot

oneCount = 0
twoCount = 0
threeCount = 0
fourCount = 0
fiveCount = 0
sixCount = 0
sevenCount = 0
eightCount = 0
nineCount = 0
tenCount = 0
elevenCount = 0
twelveCount = 0
thirteenCount = 0
fourteenCount = 0
fifteenCount = 0
sixteenCount = 0
seventeenCount = 0
eighteenCount = 0 
nineteenCount = 0
twentyCount = 0


while True: #Main loop
    print("Hello, do you want to generate a random spread between 1-20, (y)es or (n)o?")
    while True: #User input loop.
        userAnswer = input()
        if userAnswer == 'n':
            sys.exit() # Quit the program.
        if userAnswer == 'y':
            break # Break out of the player input loop.
    while True: #Iteration Loop
        print("Current Totals: ")
        print("%s Ones  %s Twos %s Threes %s Fours %s Fives" % (oneCount, twoCount, threeCount, fourCount, fiveCount))
        print("%s Sixes  %s Sevens %s Eightss %s Niness %s Tens" % (sixCount, sevenCount, eightCount, nineCount, tenCount))
        print("%s Elevens  %s Twelves %s Thirteen %s Fourteen %s Fifteen" % (elevenCount, twelveCount, thirteenCount, fourteenCount, fifteenCount))
        print("%s Sixteens  %s Seventeens %s Eighteens %s Nineteens %s Twenties" % (sixteenCount, seventeenCount, eighteenCount, nineteenCount, twentyCount))
        print("How many iterations should we run?")
        iterationCount = int(input())
        if iterationCount <= 0:
            print("Cannot run 0 or less iterations, generating chart.")
            Number = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
            Totals = [oneCount,twoCount,threeCount,fourCount,fiveCount,sixCount,sevenCount,eightCount,nineCount,tenCount,elevenCount,twelveCount,thirteenCount,fourteenCount,fifteenCount,sixteenCount,seventeenCount,eighteenCount,nineteenCount,twentyCount]
            plot.bar(Number,Totals)
            plot.title('Number Spread for Generated Numbers')
            plot.xlabel('Numbers')
            plot.ylabel('Totals')
            plot.show()
        elif iterationCount >= 0:
            while iterationCount >= 0:
                randomNumber = random.randint(1,20)
                iterationCount = iterationCount - 1
                if randomNumber == 1:
                    oneCount = oneCount + 1
                elif randomNumber == 2:
                    twoCount = twoCount + 1
                elif randomNumber == 3:
                    threeCount = threeCount + 1
                elif randomNumber == 4:
                    fourCount = fourCount + 1
                elif randomNumber == 5:
                    fiveCount = fiveCount + 1
                elif randomNumber == 6:
                    sixCount = sixCount + 1
                elif randomNumber == 7:
                    sevenCount = sevenCount + 1
                elif randomNumber == 8:
                    eightCount = eightCount + 1
                elif randomNumber == 9:
                    nineCount = nineCount + 1
                elif randomNumber == 10:
                    tenCount = tenCount + 1
                elif randomNumber == 11:
                    elevenCount = elevenCount + 1
                elif randomNumber == 12:
                    twelveCount = twelveCount + 1
                elif randomNumber == 13:
                    thirteenCount = thirteenCount + 1
                elif randomNumber == 14:
                    fourteenCount = fourteenCount + 1
                elif randomNumber == 15:
                    fifteenCount = fifteenCount + 1
                elif randomNumber == 16:
                    sixteenCount = sixteenCount + 1
                elif randomNumber == 17:
                    seventeenCount = seventeenCount + 1
                elif randomNumber == 18:
                    eighteenCount = eighteenCount + 1
                elif randomNumber == 19:
                    nineteenCount = nineteenCount + 1
                elif randomNumber == 20:
                    twentyCount = twentyCount + 1