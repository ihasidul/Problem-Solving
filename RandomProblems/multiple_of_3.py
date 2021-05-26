#Write a program that prints out the multiples of 3 till n

def get_total_multiples_of_3(n):
    for number in (range(n)):
        if(number % 3 == 0):
            print(number)
        else:
            continue
get_total_multiples_of_3(200)

