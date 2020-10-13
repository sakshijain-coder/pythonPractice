sum = 0
count = 0
while (1):
    num = input("enter number:")
    if(num=="q"):
        break;
    sum+=int(num)
    count+=1
avg=sum/count
print("Average of total number is:",avg)
