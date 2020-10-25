def isAnagram( s, t):
        if len(s)!=len(t):
            return False;
        s=sorted(s)
        t=sorted(t)
        for i in range(0,len(s)):
            if (s[i] != t[i]):
                return False
        return True
str1=input("Enter 1st String:")
str2=input("Enter 2nd String:")
print("Anagram" if isAnagram(str1,str2) else "Not Anagram")
