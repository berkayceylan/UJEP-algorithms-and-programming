numbers = []
even = 0
odd = 0

n = int(input("Enter the count.\n"))

print("Write numbers")

for i in range(0, n):
    number = int(input())
    numbers.append(number)

print("The list is: " + str(numbers))

for numb in numbers:
    if(numb % 2 == 0):
        even += 1
    else:
        odd += 1

print("Event count is: " + str(even) + "\nOdd count is: " + str(odd))