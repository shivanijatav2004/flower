age = 25
##nexting condition
if(age >= 18):
    if(age >= 70):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")  

#qution even odd num print
num = int(input("enter number :"))
rem = num % 2
if(rem == 0):
    print("even")
else:
    print("odd")          

## greatest num print
a = int(input("enter first number:"))
b = int(input("enter second number : "))
c = int(input("enter third number : "))
if(a >= b and a >= c):
    print("first is number greatest", a)
elif(b >= a and b >= c):
    print("second is number greatest", b) 
else:
    print("third is number greatest", c) 

## 4  greater num print
a = int(input("enter first number:"))
b = int(input("enter second number : "))
c = int(input("enter third number : "))
d = int(input("enter foruth number :"))
if(a >=b and a >= c and a>= d):
    print("frist is number greater", a)
elif(b >= a and b >= c and b >= d):
    print("second is number greater", b)
elif(c >=a and c >= b and c >= d):
    print("third is number greater", c)
else:
    print("fourth is dnumber greater", d)


##multiple 7 print
x = int(input("enter number : "))
if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")