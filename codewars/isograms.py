import string
def is_isogram(str):
    if len(str) == 0:
        return True
    alphabet = dict.fromkeys(string.ascii_lowercase, 0)
    str = str.lower()
    word=[]
    word[:0] = str
    for letter in word:
        alphabet[letter] = alphabet[letter] + 1
    for letter in alphabet:
        if (alphabet[letter] > 1):
            return False
    return True