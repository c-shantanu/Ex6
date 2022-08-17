# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


### Task 1 - fix the FizzBuzz

three_mul = 'fizz'
five_mul = 'buzz'
num1 = 3
num2 = 5
max_num = 100
   
for i in range(1,max_num):
    # % or modulo division gives you the remainder 

    if i%num1 == 0 and i%num2 == 0:
        print(i, three_mul+five_mul)
    
    elif i%num1 == 0:
        print(i, three_mul)

    elif i%num2 == 0:
        print(i, five_mul)

### Task 2 - Summing integers

n = 5
number = 1
sum = 0
while number < n + 1:
    sum = sum + number
    number = number + 1
print("Sum =", sum)

### Task 3 - summing integers with range()

n = 6
sum = 0
for num in range(n):
    sum += num
print("Sum =", sum)

### Task 4 - Printing in loops

#Program no. 1
for x in range(3):
    print(x)

#Program no. 2
for j in range(5):
    print("This is loop number", j)

#Program no. 3
x = 10
while x > 0:
    print(x)
    x -= 1

#Program no.4
countdown = 5
while countdown:
    print(f"{countdown}")
    countdown -= 1
else:
    print("Start!")


### Task 5 - Summing three integers
x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x == y or y == z:
    result = 0
    print("Calculated sum is ", result)
else:
    sum = x + y + z
    print("Calculated sum is", sum)




### Task 7 - Swapping variables
a = input("First value for a: ")
b = input("Second value for b: ")

print("Before swapping: a =", a)
print("Before swapping: b =", b)

temp = a
a = b
b = temp

print("After swapping: a =", a)
print("After swapping: b =", b)

### Task 8 - max and min values
x = float(input("First number: "))
y = float(input("Second number: "))
z = float(input("Third number: "))

print("The maximum value is ", max(x, y ,z))
print("The minimum value is ", min(x, y ,z))


### Task 9 - Conversion
x = int(input("Type your value: "))

if x == 0:
    x = False
elif x == 1:
    x = True
else:
    pass

print("Your entered value is now ", x)

### Task 10 - Divisible number
x = int(input("First number: "))
y = int(input("Second number: "))

if x % y == 0:
    print("First number is divisible by second number, result =", x // y)
elif y % x == 0:
    print("Second number is divisible by first number, result =", y // x)
else:
    print("Numbers are non-divisible!")

