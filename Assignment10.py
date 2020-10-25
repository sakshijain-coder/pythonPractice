list1=[1,2,8,4,2,6,4,10,10,10]
list2=[]
for elem in list1:
    if(list2.__contains__(elem)==False):
        list2.append(elem)
print("list with duplicate item:",list1)
print("list with unique element:",list2)
