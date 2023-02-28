import random

#1. generate a list of random numbers
numbers = []
for i in range(1,5):
    numbers.append(random.randint(1,100))
#for testing - DELETE!! //@@
numbers.append(5)
print(numbers)

#2. find the first prime number in the list
#[10,11,12,13]
for x in numbers:
    is_prime = True
    for y in range(2,x):
        if x%y==0:
            is_prime = False
            break
        # print("check another divider...")
    if is_prime == True:
        print(f"first prime is {x}")
        break
    # print("keep looking...")

    
#3. print the number (or message that there is no such number)
