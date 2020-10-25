def isPangram(str):
    letter = set({})
    for i in range(0 , len(str)):
        if(str[i].isalpha()):
            letter.add(str[i])
    if len(letter)==26:
        return True
    else:
        return False
str=input("Enter String:")
print("Pangram" if isPangram(str) else "Not Pangram")
