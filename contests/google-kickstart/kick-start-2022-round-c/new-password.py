import re
t = int(input())
tc = 0
for i in range(t):
    len_of_given_pass = int(input())
    given_pass = input()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alphaUpper = alpha.upper()
    special = "#@*&"
    numbers = "0123456789"
    # check for length
    if not re.search("[a-z]", given_pass):
        given_pass = given_pass + alpha[0]
    if not re.search("[A-Z]", given_pass):
        given_pass = given_pass + alphaUpper[0]
    if not re.search("[0-9]", given_pass):
        given_pass = given_pass + numbers[0]
    if not re.search("[#@*&]", given_pass):
        given_pass = given_pass + special[0]
    if len(given_pass) < 7:
        given_pass = given_pass + alpha[0:7-len(given_pass)]
    print("Case #"+ str(i+1) + ": {}".format(given_pass))
