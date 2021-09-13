
# def helper(S):
#     substring = 'abb'
#     if substring in S:
#         S = S.replace(substring, 'baa')
#         print("if",S)
#         helper(S)
#     elif substring not in S:
#         print(type(S))
#         print("In else",S)
#         print("In else",type(S))
#         return S
def helper(s):
    s = s.replace('abb', 'baa')
    return s
def solution(S):
    substring = 'abb'
    while substring in S:
        S = helper(S)
    return S

    # write


    
print(solution('ababb'))
# print(solution('ababb'))