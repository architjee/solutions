OP_DIC= {
    '/': lambda x, y: x//y,
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y
}
stk = []
s = input().split()
for token in s:
    if token in OP_DIC:
        operand1 = stk.pop()
        operand2 = stk.pop()
        # print("Operating ", token, " on ", operand1, open)
        result = OP_DIC[token](operand2, operand1)
        stk.append(result)
    else:
        stk.append(int(token))
print(stk[-1])