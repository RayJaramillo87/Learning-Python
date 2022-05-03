import random,sys
from tkinter import Y
from xml.dom.minidom import Element
import matplotlib.pyplot as plot

randomSpread = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

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
        print("%s Ones  %s Twos %s Threes %s Fours %s Fives" % (randomSpread[0], randomSpread[1], randomSpread[2], randomSpread[3], randomSpread[4]))
        print("%s Sixes  %s Sevens %s Eightss %s Niness %s Tens" % (randomSpread[5], randomSpread[6], randomSpread[7], randomSpread[8], randomSpread[9]))
        print("%s Elevens  %s Twelves %s Thirteen %s Fourteen %s Fifteen" % (randomSpread[10], randomSpread[11], randomSpread[12], randomSpread[13], randomSpread[14]))
        print("%s Sixteens  %s Seventeens %s Eighteens %s Nineteens %s Twenties" % (randomSpread[15], randomSpread[16], randomSpread[17], randomSpread[18], randomSpread[19]))
        print("How many iterations should we run?")
        iterationCount = int(input())
        if iterationCount <= 0:
            TotalIteration = 0 
            for i in range (0, len(randomSpread)):
                TotalIteration = TotalIteration + randomSpread[i]    
            print("Cannot run 0 or less iterations, generating chart.")
            print("Total Iterations Ran: " + str(TotalIteration))
            Number = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']            
            Totals = [float(randomSpread[0]/TotalIteration),float(randomSpread[1]/TotalIteration),float(randomSpread[2]/TotalIteration),float(randomSpread[3]/TotalIteration),\
                float(randomSpread[4]/TotalIteration),float(randomSpread[5]/TotalIteration),float(randomSpread[6]/TotalIteration),float(randomSpread[7]/TotalIteration),\
                    float(randomSpread[8]/TotalIteration),float(randomSpread[9]/TotalIteration),float(randomSpread[10]/TotalIteration),float(randomSpread[11]/TotalIteration),\
                        float(randomSpread[12]/TotalIteration),float(randomSpread[13]/TotalIteration),float(randomSpread[14]/TotalIteration),\
                            float(randomSpread[15]/TotalIteration),float(randomSpread[16]/TotalIteration),float(randomSpread[17]/TotalIteration),\
                                float(randomSpread[18]/TotalIteration),float(randomSpread[19]/TotalIteration)]
            plot.bar(Number,Totals)
            plot.title('Number Spread for Generated Numbers')
            plot.xlabel('Numbers')
            plot.ylabel('Totals')
            plot.show()
        elif iterationCount > 0:
            while iterationCount > 0:
                randomNumber = random.randint(1,20)
                iterationCount = iterationCount - 1
                if randomNumber == 1:
                    randomSpread[0] = randomSpread[0] + 1
                elif randomNumber == 2:
                    randomSpread[1] = randomSpread[1] + 1
                elif randomNumber == 3:
                    randomSpread[2] = randomSpread[2] + 1
                elif randomNumber == 4:
                    randomSpread[3] = randomSpread[3] + 1
                elif randomNumber == 5:
                    randomSpread[4] = randomSpread[4] + 1
                elif randomNumber == 6:
                    randomSpread[5] = randomSpread[5] + 1
                elif randomNumber == 7:
                    randomSpread[6] = randomSpread[6] + 1
                elif randomNumber == 8:
                    randomSpread[7] = randomSpread[7] + 1
                elif randomNumber == 9:
                    randomSpread[8] = randomSpread[8] + 1
                elif randomNumber == 10:
                    randomSpread[9] = randomSpread[9] + 1
                elif randomNumber == 11:
                    randomSpread[10] = randomSpread[10] + 1
                elif randomNumber == 12:
                    randomSpread[11] = randomSpread[11] + 1
                elif randomNumber == 13:
                    randomSpread[12] = randomSpread[12] + 1
                elif randomNumber == 14:
                    randomSpread[13] = randomSpread[13] + 1
                elif randomNumber == 15:
                    randomSpread[14] = randomSpread[14] + 1
                elif randomNumber == 16:
                    randomSpread[15] = randomSpread[15] + 1
                elif randomNumber == 17:
                    randomSpread[16] = randomSpread[16] + 1
                elif randomNumber == 18:
                    randomSpread[17] = randomSpread[17] + 1
                elif randomNumber == 19:
                    randomSpread[18] = randomSpread[18] + 1
                elif randomNumber == 20:
                    randomSpread[19] = randomSpread[19] + 1