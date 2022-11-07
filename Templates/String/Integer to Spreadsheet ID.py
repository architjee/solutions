import string
upperCaseLetters = '0'+string.ascii_uppercase
# We are given the following test cases:
# f(4)=>'D'
# f(27)=>'AA'
# f(702)=>'ZZ'
# Creating additional test cases:
# f(1)=>'A'
def f(num_as_int):
    def construct_from_base(num_as_int, base):
        return '' if num_as_int==0 else construct_from_base(num_as_int//base, base)+upperCaseLetters[num_as_int%base]
    return construct_from_base(num_as_int, 26)
print(f(4))
print(f(27))
print(f(702))
print(f(1))
print(f(4))
