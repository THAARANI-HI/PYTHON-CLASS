#Find even and odd numbers from a list, and store them separately in a new list

list=[22,37,84,55,78,94,45,10,63]
odd_list=[]
even_list=[]

for i in list:
    if i%2==0:
        even_list.append(i)
    else:
         odd_list.append(i)
print(even_list)
print(odd_list)