#https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
#6 kyu
def to_camel_case(text):
    s = text.replace("-", " ").replace("_", " ")
    s = s.split()
    if len(text) == 0:
        return text
    return s[0] + ''.join(i.capitalize() for i in s[1:])
print(to_camel_case("the_stealth_warrior"))


