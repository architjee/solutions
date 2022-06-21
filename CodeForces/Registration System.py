n = int(input())
d = {}
for i in range(n):
    text = input();
    if text in d:
        d[text] +=1;
        print(text+str(d[text]))
    else:
        d[text] = 0;
        print("OK")