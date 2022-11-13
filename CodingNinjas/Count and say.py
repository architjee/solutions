def writeAsYouSpeak(n):
    # Write your code here.
    def next_number(s):
        result =[]
        i,count=0,1
        while i<len(s):
            while i+1<len(s) and s[i]==s[i+1]:
                i+=1
                count+=1
            result.append(str(count)+s[i])
            count  = 1
            i+=1
        return ''.join(result)
    s='1'
    for i in range(1, n):
        s=next_number(s)
    return s
print(writeAsYouSpeak(5))