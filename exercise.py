a = 1
for i in range(5):
    for j in range(a):
        print("*", end="")
    a = a + 1      
    print("")
for i in range(5):
    for j in range(a):
        print("*", end="")
    a = a - 1     
    print("")