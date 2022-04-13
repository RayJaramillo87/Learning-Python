def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result


print('Please insert a number: ')
try:
    number = int(input())
except ValueError:
    print('You must enter a whole Integer.')
count = 0
while number != 1:
    number = collatz(int(number))
    count = count + 1

print('Count: ' + str(count))