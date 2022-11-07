import string
upperCaseLetters = string.ascii_uppercase
# We are given the following test cases:
# f(4)=>'D'
# f(27)=>'AA'
# f(702)=>'ZZ'
# Creating additional test cases:
# f(1)=>'A'
def f(num_as_int):
    def construct_from_base(num_as_int, base):
        if num_as_int==0:
            return ''
        appendage=''
        if not num_as_int%base:
            appendage='Z'
        else:
            appendage=upperCaseLetters[num_as_int%base-1  ]
        return construct_from_base(num_as_int//base, base)+appendage
    return construct_from_base(num_as_int, 26)
print(f(4))
print(f(26))
print(f(27))
print(f(701))
print(f(702))
print(f(1))
print(f(4))
