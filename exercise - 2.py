word = []

n = int(input("Enter the count."))

for i in range(0, n):
    letter = input()
    word.append(letter)

print("World is " + str(word))

word.reverse()

print("Reversed version is" + str(word))