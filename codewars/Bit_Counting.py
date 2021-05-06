#https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python
#6kyu

def count_bits(n):
    binary_of_n = bin(n).replace("0b", "")
    list_of_digits = map(int,binary_of_n)
    return sum(list_of_digits)

print(count_bits(7))