# r, r+ read - write (can't create file), w, w+ truncated - over-written, a, a+ append only,
# open(r"name", "access_mode")
# file1 = open ("MyFile1", "w")
# file1.write("test write")
# file1.writelines(["test 1\n", "test2\n"]) 
# file1.read()
# file1.readline()
# file1.readlines()
# file1.close()
# file.seek(0)

myFile = open("myfile", "w")
L = ["This is Delhi \n", "This is Paris\n", "This is London\n"]
myFile.write("Hello\n")
myFile.writelines(L)
myFile.close()

myFile = open("myfile", "r+")

print("Output of read function is")
print(myFile.read())
print()

myFile.seek(0)
print("Output of readline function is")
print(myFile.readline())
print()

myFile.seek(0)
print("Output of read(9) function is")
print(myFile.read(9))
print()

myFile.seek(0)
print("Output of readline(9) function is")
print(myFile.readline(9))
print()

myFile.seek(0)
print("Output of readlines function is")
print(myFile.readlines())
print()
myFile.close()

myFile = open("myfile", "a+")
myFile.write("Today\n")

myFile = open("myfile", "r")
print("Output of Readlines after appending")
print(myFile.readlines())
print()
myFile.close()

myFile = open("myfile", "w+")
myFile.write("Tomorrow\n")
myFile.seek(0)

print("Output of Readlines after writing")
print(myFile.readlines())
print()
myFile.close()

l = ["Geeks", "for", "Geeks!"]
with open ("gfg", "w+") as f:
    for items in l:
        f.write("%s\n" %items)
    print("File has written successfully!")

l = ["Geeks\n", "for\n", "Geeks!\n"]

file1 = open("test1/myfile", "w")
file1.writelines(l)
file1.close()

file1 = open("gfg", "r")
print(file1.read())
file1.close()

def readFirstLine(file, n):
    arr = file.readlines()
    print(arr)
    for i in range(n - 1):
        print(str(arr[i]))
file1 = open("gfg", "r")
readFirstLine(file1, 8)

def readFirstLine(fileName, n):
    with open(fileName) as myfile:
        head = [next(myfile) for x in range(n)]
    print(head)
def LastNlines(fname, N):
    with open(fname) as file:
        for line in (file.readlines() [-N:]):
            print(line, end ='')
readFirstLine("gfg", 3)
print("-----------")
LastNlines("gfg", 3)
print("--------------")

file1 = open("gfg", "r")
arr = file1.readlines()
print(arr)
print("-----------------")

def into_a_varaiable(fileName):
        with open (fileName, "r") as file1:
                data=file1.readlines()
                print(data)
into_a_varaiable('gfg')