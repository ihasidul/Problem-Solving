#Problem link https://www.codewars.com/kata/55908aad6620c066bc00002a
def xo(s):
    total_x  = 0
    total_o = 0
    for i in list(s):
        if(i =='x' or i == 'X'):
            total_x += 1
        elif(i =='o' or i == 'O'):
            total_o += 1
            
    return total_x == total_o
