import random

d = input("Введите свое имя: ")
b = ""
i=0
while i<3:
    b += (chr(random.randint(97,122)))
    i+=1
i=0
while i<2:
    b += (chr(random.randint(65,90)))
    i+=1
if (len(d)%100)>9:
    b += len(d) % 100
else:
    b += "0"
    b += str(len(d) % 100)
with open("pas.txt", "a", encoding="UTF-8") as file:
    file.write(f"\n{d}-{b}")
print(b)
