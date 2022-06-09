x=int(input("podaj pierwszą liczbe:"))
y=int(input("podaj drugą liczbe:")) 
while x>y or x<y:
    if x>y:
        x=x-y
    elif x<y:
        y=y-x
print(x)
