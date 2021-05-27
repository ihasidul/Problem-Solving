#Write a function that will receive a string as an input and will return the string in reverse order
def reverse_string(s):
    return s [::-1]
def another_reverse_string(s):
    s_len = len(s)
    result = ""
    while(s_len >= 0):
        result += s[s_len]
        s_len -= 1


    return result
print(another_reverse_string("Hekko"))
