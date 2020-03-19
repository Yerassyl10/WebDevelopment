def count_code(str):
    r=0
    for i in range(len(str)-3):
        if str[i:i+2]=='co' and str[i+3]=='e': r+=1
    return r
