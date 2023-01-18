# def person_color(name, color):
#     print(f"{name} likes {color}")

# name = input("What is your name?\n")
# color = input("What is your favorite color?\n")

# person_color(name, color)

# def kgToPounds(kg):
#     return kg * 2.2

# kg = int(input("What is your kg?"))

# print("Pounds is: " + str(kgToPounds(kg)))

# def housePrice(goodCredit):
#     if(goodCredit):
#         return 1000000 - (1000000 * 10 / 100)
#     else:
#         return 1000000 - (1000000 * 20 / 100)

# print(housePrice(True))
# print(housePrice(False))

# def nameCheck(name):
#     if(len(name) < 4):
#         print("It is too short")
#     elif(len(name) > 55):
#         print("It is to long")
#     else:
#         print("The name is good")

# name = input("Write a name\n")
# nameCheck(name)

# def weight(type, amount):
#     if(type == "K"):
#         print("You are " + amount + " kilograms")
#     elif(type == "L"):
#         print("You are " + amount + " pounds")

# type = input("Kg or pounds")
# amount = input("Write your weight")
# weight(type, amount)

# def guessGame():
#     trytime = 0
#     number = 5
#     guessedNumber = 0
    # while (guessedNumber != number and trytime < 3):
#         trytime += 1
#         guessedNumber = int(input("Guess a number"))
    
#     if(trytime != 3 or guessedNumber == number):
#         print("You won!")
#     else:
#         print("Sorry!")

# guessGame()


# def lenOfString(str):
#     counter = 0
#     for lett in  str:
#         counter += 1
#     return counter

# print('Length of "lesson" ' + str(lenOfString("lesson")))

# def numberOfChars(str1):
#     counter = 0
#     counterChar = 0
    
#     charList = []

#     for char1 in str1:
#         char = str1[counter]
#         if not char in charList:
#             for char2 in str1:
#                 if(char2 == char):
#                     counterChar += 1
#                 charList.append(char2)
#         print(str(char) + " : " + str(counterChar))
#         counter += 1
#         counterChar = 0
# def numberOfChars(str1):
#     charList = []
#     for char in str1:
#         if not (char in charList):
#             print(char + ": " + str(str1.count(char)))
#         charList.append(char)
# numberOfChars("Beeerkayy") 
# numberOfChars("Berkay")

# def first2last2(mystr):
#     if(len(mystr) < 3):
#         print(mystr + mystr)
#     else:
#         print(mystr[0:2] + mystr[len(mystr) - 2 : len(mystr)])

# first2last2("l")

# def removeFirstLetter(mystr):
#     firstChar = mystr[0]
#     newStr = mystr.replace(firstChar, "$")
#     print(firstChar + newStr)

# removeFirstLetter("baaabcbcbrtybbbb")

# def changeCharFromString(myString, inx1, inx2):
#     strList = list(myString)
#     temp = strList[inx1]
#     strList[inx1] = strList[inx2]
#     strList[inx2] = temp
#     return "".join(strList)

# def changeStrings(myStr):
#     stringList = myStr.split(" ")
    
#     temp = stringList[0]
#     stringList[0] = stringList[1]
#     stringList[1] = temp

#     newString = ""
#     for item in stringList:
#         itemStr = changeCharFromString(item, 0, 1)
#         newString += itemStr + " "
#     print(newString)

# changeStrings("Berkay Ceylan")

# def addIng(myStr):
#     if(len(myStr) < 3):
#         return myStr
#     elif(myStr[3:] == "ing"):
#         return myStr + "ly"
#     else:
#         return myStr + "ing"


# print(addIng("be"))
# print(addIng("abc"))
# print(addIng("string"))

# def changeNotPoor(myStr):
#     if("not" in myStr):
#         searchString = myStr[myStr.find("not") : len(myStr)]
#         if("poor" in searchString):
#             return myStr.replace(myStr[myStr.find("not") : myStr.find("poor") + 4], "good")
#         else:
#             return myStr
#     else:
#         return myStr
# myStr = "the song is not that poor" 
# print(changeNotPoor(myStr))

