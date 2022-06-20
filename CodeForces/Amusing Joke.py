hostName = input()
residenceName =input()
jumbledLetters = input()
if(sorted(hostName+residenceName)==sorted(jumbledLetters)):
    print("YES")
else:
    print("NO")