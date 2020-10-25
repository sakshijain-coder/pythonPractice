list1=[1,2,3,4,5]
list2=[4,5,3]
list3=[]
if(len(list1)<=len(list2)):
    for elem in list1:
        if (list2.__contains__(elem)):
            list3.append(elem)
else:
    for elem in list2:
        if (list1.__contains__(elem)):
            list3.append(elem)
print("common element is:",list3)
