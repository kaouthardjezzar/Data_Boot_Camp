path = "./students_names.txt"

#Read all of the content of the file in one variable.
file = open(path)

names = file.read()
print(names)

file.close()

#Write a list of random names to your file.

list_name=["Kawther Djezzar", "Lila Berkani", "Anis Belambri", "Anfel Djezzar", "Tinhinane Chafai", "Ines Chafa"]

for name in list_name :
    names = names + "\n" + name

file = open(path, 'w')
file.write(names)
file.close()

#Read the first n lines of the file.

n = 3
file = open(path)

for i in range (n) :
    line = file.readline()
    print (line)
file.close

#Read the last n lines of the file.
n = 4
file = open(path, "r")
lines = file.readlines()
last_lines = lines[-n:]
for line in last_lines :
    print(line)
file.close

#Check if the name x is in the file

name = 'Kawther Djezzar'
file = open(path, "r")
lines = file.read().splitlines()
print (name in lines)
file.close()