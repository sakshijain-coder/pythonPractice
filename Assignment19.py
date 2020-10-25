num=int(input("Enter Number:"))
rev_num=0
while(num):
    rev_num=rev_num*10+num%10
    num=int(num/10)

print("Reverse Number is:",rev_num)
