a = 12
s = "Hello"
try :
    print ("inside try")
    print (a + s)
    print ("printed using original data types")
except TypeError :
    print ("inside except")
    print (str(a) + s)
    print ("printed using type-casted data types")

    