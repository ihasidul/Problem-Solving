#https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
#7kyu
def high_and_low(numbers):
    arr = numbers.split()
    arr = [int(i) for i in arr]
    arr.sort()
    #Aprint(str(arr[0]) + " " + str(arr[-1]))
    return str(arr[-1]) + " " + str(arr[0])


#print(high_and_low("1 2 3 4 5")) # return "5 1"
#print(high_and_low("1 2 -3 4 5")) # return "5 -3"
print(high_and_low("1 9 3 4 -5")) # return "9 -5"
high_and_low("5 34 2 5432 2 1 2 3 4 5")
