
print("zadanie 3.1")

word = "Swierzy"
print(word)

print("+---+---+---+---+---+---+---+")
print("| {} | {} | {} | {} | {} | {} | {} |".format(word[0],word[1],word[2],word[3],word[4],word[5],word[6]))
print("+---+---+---+---+---+---+---+")

print("zadanie 3.2")
print("--------------------")
print("for")
print("--------------------")

for x in range(1, 41):
    if x!=13:
        print(x)
        if x%5==0:
            print(str(x) + " is devided by 5")
        if x%7==0:
            print(str(x) + " is devided by 7")
        if x%5!=0 and x%7!=0:
            print(str(x) + " is not important")
print('-----------------')
print("while")
print("------------------")
i=1
while i < 41:
    if i != 13:
        print(i)
        if i % 5 == 0:
            print(str(i) + " is devided by 5")
        if i % 7 == 0:
            print(str(i) + " is devided by 7")
        if i % 5 != 0 and i % 7 != 0:
            print(str(i) + " is not important")
    i += 1



print("Zadanie 3.3")

outfile = open("vars.txt",'w')
n = 2022
import math
x = math.pi
word = "Python"
english = "book"

outfile.write("{}\n{:.5f}\n{}\n{}\n".format(n,x,word,english) )
outfile.close()

file = open("vars.txt", "r")
for line in file:
    print(line)
file.close()


