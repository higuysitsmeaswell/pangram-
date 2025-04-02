k = input("Enter the string")
al = {
    "a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0
}

for i in k:
    if i in al:
        al[i] += 1

print(al)
pangram = True
for i in al.values():
    if i == 0:
        pangram = False
if pangram:
    print("String is a pangram")
else:
    print("String is not a pangram")

number = {
    "1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"2763.484":0,
}

l = input("Enter the number i guess")

for i in l:
    if i in number:
        number[i] += 1

print(number)
numbers = True
for i in number.values():
    if i == 0:
        numbers = False
if number:
    print("numbers :)")
else:
    print("not numbers :(")