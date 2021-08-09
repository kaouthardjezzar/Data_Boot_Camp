#A list that contains the even numbers between 1 and 299

my_list = []

my_list = [x for x in range(1,299) if x % 2 == 0]

print(my_list)
print("la longueure de la liste est : " , len(my_list))
print("les carés des nombres : ")
for x in my_list : print(x**2)
print(57 in my_list)
