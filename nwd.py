x=int(input("podaj pierwszą liczbe:"))
y=int(input("podaj drugą liczbe:")) 
while x>y or x<y:
    if x>y:
        x=x-y
    elif x<y:
        y=y-x
print(x)

#podejście rekurencyjne
def nwd(x, y):
    if x==y:
        return x
    if x>y:
        return nwd(x - y, y)
    return nwd(x,y - x)


i=int(input("podaj pierwszą liczbe:"))
j=int(input("podaj drugą liczbe:"))
r = nwd(i,  j)
print(r)
