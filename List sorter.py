#To insert a random list and sort it in ascending order
l=[]
x=int(input("Enter first element"))
y=int(input("Enter second element"))
z=int(input("Enter third element"))
e=int(input("Enter fourth element"))
f=int(input("Enter fifth element"))
l.append(x)
l.append(y)
l.append(z)
l.append(e)
l.append(f)
i=0
for i in range(i,len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print("The sorted list is",l)