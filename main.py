def calcR(lr):
    s = 0
    for el in lr:
        s = s + int(el)
    return s

def calcT(lt):
    s1 = 0
    s2 = 9
    s3 = 0
    for i in range(100):
        z = 3*i
        if int(lt[z]) == 10:
            s1 = s1 + 1
        elif int(lt[z+1]) == 10:
            s2 = s2 + 1
        elif int(lt[z+2]) == 10:
            s3 = s3 + 1
        else:
            print(">>> Error")
    print(s1)
    print(s2)
    print(s3)

file = open("r.txt", "r")
content = file.read()
tokens = content.split()
countT = 0
for el in tokens:
    countT = countT + 1
print(countT)

s = 0
c1 = []
c2 = []
c3 = []

print(tokens)
print()

for i in range(100):
    z = 3*(i)
    max = z
    #print(i)
    #print(tokens[z])
    #print(tokens[z+1])
    #print(tokens[z+2])
    #print()
    if (int(tokens[z]) == 10 and int(tokens[z+1]) == 10):
        tokens[z] = "9"
    if (int(tokens[z+2]) == 10 and int(tokens[z+1]) == 10):
        tokens[z+2] = "9"
    if (int(tokens[z]) == 10 or int(tokens[z+1]) == 10 or int(tokens[z+2]) == 10):
        pass
    if int(tokens[z]) < int(tokens[z+1]):
        max = z + 1
    if int(tokens[max]) < int(tokens[z+2]):
        max = z + 2
    tokens[max] = "10"

print(tokens)

for el in tokens:
    s= s+1
    if s > 3:
        s = 1
    match s:
        case 1:
            c1.append(el)
        case 2:
            c2.append(el)
        case 3:
            c3.append(el)

print(calcR(c1))
print(calcR(c2))
print(calcR(c3))

calcT(tokens)

file.close()
