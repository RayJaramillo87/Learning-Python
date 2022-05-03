def commaCode(inputList):
    try:
        if len(inputList) >= 1:
            for i in inputList:
                if inputList.index(i) < len(inputList) - 1:
                    print(i + ',')
                else: 
                    print(i + ', and ' + inputList[-1])
        elif len(inputList) <= 0:
            print("Cannot run against empty list!")

    except ValueError:
        print('Error Error Error')
