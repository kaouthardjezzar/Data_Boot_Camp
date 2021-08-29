import string

#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)

for i in alphabet_list :
    name = "./Question6/"+str(i)+".txt"
    file = open(name, 'w+')