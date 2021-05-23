import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = dict.fromkeys(string.ascii_lowercase, 0)
        if(len(sentence) < 26):
            return False
        else:
            for i in list(sentence):
                alphabet[i] = alphabet[i] + 1
            return all( x > 0 for x in alphabet.values())
