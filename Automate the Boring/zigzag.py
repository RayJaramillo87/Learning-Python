import time, sys, random
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.
try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('Leti Leti Leti Leti cant you see sometimes your words just hypnotize me!')
        time.sleep(0.25) # Pause for 1/10 of a second.
        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + random.randint(1,5)
            if indent >= 75:
                # Change direction:
                indentIncreasing = False
        else:
            # Decrease the number of spaces:
            indent = indent - random.randint(1,5)
            if indent <= 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()