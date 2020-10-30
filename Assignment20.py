def isArithmaticProgress(list):
    diff=list[1]-list[0]
    for i in range(2,len(list)):
        if(list[i]-list[i-1]!=diff):
            return False
    return True

list=[5,7,9,13]
print(isProgress(list))
