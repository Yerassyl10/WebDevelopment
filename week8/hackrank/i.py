def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print (result)

