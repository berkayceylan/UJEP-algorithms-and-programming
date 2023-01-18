def sequence():
    for i in range(1000):
        print((i ** 2) - (3 * i) + 6)

# sequence()

# def GetNthLetters(text, n):
#     builtstring = ""
#     lengText = int(len(text))
#     for i in range(0, lengText):
#         if (i + 1) % n == 0:
#             builtstring = builtstring + text[i]
#     return builtstring

# a = input("Something: ")

# print(GetNthLetters(a, 4))



# czechFile = open("czechLang", "r")
# czechWords = czechFile.readlines()



# engFile = open("engLang", "r")
# engWords = engFile.readlines()

# dict = {czechWords[i].strip(): engWords[i].strip() for i in range(len(czechWords))}

# word = input("Write a word")


# print(dict[word])

# while True:
#     try:
#         x = int(input("Please write a number: "))
#         break
#     except ValueError:
#         print("It's not number!")

# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

# while True:
#     try:
#         x = int(input("Please write a letter: "))
#         break
#     except ValueError:
#         print("It's not letter!")

# while True:
#     try:
#         x = ord(input("Please write a letter: "))
#         break
#     except TypeError:
#         print("It's not letter!")

# try:
#     x = 1 / 0
# except ZeroDivisionError as err:
#     print("Handling runtime error:", err)

# dictWeather = {
#     "usti": "15",
#     "prague": "13",
#     "brno": "14"
# }

# try:
#     city = input("City: ")
#     print(dictWeather[city])
# except KeyError:
#     print("There is no city")


# def merge_two_dicts(x, y):
#     z = x.copy()   
#     z.update(y)    
#     return z

# first = {
#     "Berkay": 100,
#     "Micheal": 90,

# }

# second = {
#     "George": 80,
#     "Dennis": 70
# }
# lastDict = merge_two_dicts(first, second)

# for key in lastDict:
#     print(key)

def createDict(x):
    finalDict = {}

    for i in range(x):
        finalDict[i] = i ** 2
    return finalDict

print(createDict(6))