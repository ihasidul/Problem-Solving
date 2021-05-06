#https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
#7kyu
def filter_list(l):
    new_list  = []
    for i in l:
        if type(i) == int:
            new_list.append(i)
    return new_list

print(filter_list([1,2,1,2,'f','r']))

