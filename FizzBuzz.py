num = int(input("Enter a number between 1 and 100: "))

for fb in range(num+1):
    if fb % 3 == 0 and fb % 5 == 0:
        print("FizzBuzz")
    elif fb % 3 == 0:
        print("Fizz")
    elif fb % 5 == 0:
        print("Buzz")
    else:
        print(fb)