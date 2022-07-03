def getZeroPadding(n):
    if(n<10):
        return "0"+str(n)
    return str(n)
n = int(input());
print(str(21+(n//60))+":"+getZeroPadding(n%60))