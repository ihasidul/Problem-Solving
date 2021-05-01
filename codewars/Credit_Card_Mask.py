#https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python
#7kyu
# return masked string
def maskify(cc):

    if(len(cc)>4):
        last_four_digit = cc[-4:]
        number_of_hashtag = len(cc) - 4
        masked_string = ("#" * number_of_hashtag) + last_four_digit
        return masked_string
    else:
        return cc
cc = 'SF$SDfgsd2eA'

print(maskify(cc))
