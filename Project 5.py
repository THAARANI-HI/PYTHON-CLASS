# Project:Multiple table
# 1 TO 10 TABLE 12 ROWS

number=1
while number<=10:
    row=1
    while row<=12:
        print(number,"x",row,"=",number*row)
        row+=1
    number+=1
    print("     ")