def mutate_string(string, position, character):
    s_list = list(string)
    s_list[position] = character
    
    return "".join(s_list)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
