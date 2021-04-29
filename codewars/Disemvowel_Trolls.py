#Disemvowel Trolls
#https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
#7kyu
def disemvowel(string_):
    list1 = []
    list1=list(string_)
        
    for ch in range(len(list1)):
        if list1[ch] in ['a','e','i','o','u','A', 'E', 'I', 'O','U']:
            list1[ch] = ''
        else:
            continue
    listToStr = ''.join(map(str, list1))
    
    return listToStr

print(disemvowel("This website is for losers LOL!"))

