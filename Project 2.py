#Use conditional statement and get the marks
# print the result for the following marks
# 90 to 100=A grade
# 80 to 90=B grade
# 70 to 80= C grade
# 60 to 70= D grade
# below 60= E grade

#Get the student name and marks, print the total of marks,average and  give grades according to marks

tamil=int(input("enter your tamil mark: "))
english=int(input("enter your english mark: "))
maths=int(input("enter your maths mark: "))
science=int(input("enter your science mark: "))
sst=int(input("enter your sst mark: "))

total_marks=(tamil+english+maths+science+sst)
print(total_marks)

average=((tamil+english+maths+science+sst)/5)
print(average)

if average>=90 and average<=100:
    print("A grade")
elif average>=80 and average<90:
    print("B grade")
elif average>=70 and average<80:
    print("C grade")
elif average>=60 and average<=70:
    print("D grade")
else:
    print("E grade")