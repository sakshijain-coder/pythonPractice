def isPerfect(num):
    sum=0
    for i in range(1,int(num/2+1)):
        if num%i==0:
            sum+=i
    if(num==sum):
        return True
    return False
num=input("Enter Number:")
print("Perfect Number" if isPerfect(int(num)) else "Not Perfect")
