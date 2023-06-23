n=int(input("Enter a number: "))
i=1
a=0
b=1
print(a, end=" ")
print(b, end=" ")
while(i<n):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    i+=1
    

