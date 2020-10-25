def isPalindrone(str):
    n=int(len(str))
    for i in range(0,int(n/2)):
        n = n - 1
        if(str[i]!=str[n]):
            return False
    return True
str=input("Enter String:")
print("Palindrone" if isPalindrone(str) else "Not Palindrone")
