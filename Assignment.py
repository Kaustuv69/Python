
#let say you are a teacher and you have different students records containig id of the 
#student and number of subject they have taken and marks of each subject .
#You want to enter all the data in computer and want to compute the average of each student.
d={}
while True:
    d[id]=int(input("enter id"))
    num=int(input("enter the number of subjects"))
    s=0
    avg=0
    for a in range(num):
        marks=float(input("enter marks"))
        s=s+marks
        avg=s/num
    print("The student of id",d[id],"has got an average of",avg)
    done=input('Done?if yes press"y"')
    if done!="y":
        continue
    else:
        break









