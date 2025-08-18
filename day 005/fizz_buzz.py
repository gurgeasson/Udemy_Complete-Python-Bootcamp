'''
fizz buzz rules
1) program should print each number from 1 to 100 in turn and include number 100
2) when the number is divisible by 3, then instead of printing the nuber, it should print Fizz"
3) when divisible by 5, then it should print print "Buzz"
4) if the number is divisible by both (e.g. 15) print "FizzBuzz"
'''

for number in range (1, 101):
    if number % 15 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
