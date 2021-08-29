import re
#Question 1

def is_palindrome (chaine) :
    chaine = re.sub(r"\s+", "", chaine, flags=re.UNICODE)
    chaine_inverse = ""
    for i in range (len(chaine)-1, -1, -1) :
        chaine_inverse = chaine_inverse + chaine[i]

    for i in range (len(chaine)) :
        if (chaine_inverse[i] != chaine[i]):
            return False
    return True


chaine = "nurses run"
#print(is_palindrome(chaine))

#Question 2

def is_prime (n) :
    if (n == 1) : return True
    elif (n == 2) : return False
    else :
        for i in range (2,n) :
            if (n % i == 0) :
                return False
    return True

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,17,20]

#for number in numbers :
#    print (is_prime(number))

#Question 3

def is_in_range (number, min, max):
    if (number < min ) : return False
    elif (number > max ) : return True
    else : return True


#print (is_in_range(3,2,5))
#print (is_in_range(3,4,5))

#Question 4

def facto(n) :
    if (n == 0) : return 1
    elif (n == 1) : return 1
    elif (n == 2) : return 2
    else :
        fact = 1
        for i in range (2,n+1):
            fact = fact * i
        return fact

#for numb in numbers :
#    print (facto(numb))

#Question 5

def reverse_string (chaine):
    chaine_inverse = ""
    for i in range (len(chaine)-1, -1, -1) :
        chaine_inverse = chaine_inverse + chaine[i]
    return chaine_inverse

chaine1 ="kawther djezzar"
chaine2 = "Hello World!"

#print(reverse_string(chaine1))
#print(reverse_string(chaine2))

#Question 6

def sum_list(L):
    somme = 0
    for number in L :
        somme += number
    return somme

Liste1 = [1,2,3,5]
Liste2 = [20,3,2,1]

#print (sum_list(Liste1))
#print (sum_list(Liste2))

#Question 7

def max_number (L) :
    maxx = L[0]
    for i in range (1,len(L)) :
        if (L[i] > maxx) : maxx = L[i]
    return maxx

print(max_number(Liste1))
print(max_number(Liste2))