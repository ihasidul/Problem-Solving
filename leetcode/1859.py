class Solution:
    def sortSentence(self, s: str) -> str:
        result = s.split(' ')
        sentence = s.split(' ')
        for i in sentence:
            letters = list(i) 
            position = int(letters[-1])
            word = letters[:-1]
            result[position - 1] = ''.join(word)
            
        return ' '.join(result)
