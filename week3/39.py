
def to_upper(s):
    result = ""
    for char in s :
        if 'a' <= char <= 'z' :
            result += chr(ord(char) - 32)
        else : result += char
    return result

def to_lower(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else : result += char
    return result
if __name__ == "__main__":
    n = int(input())
    i = n
    while i > 0 :
        s= str(input())
        S= to_upper(s)
        x= to_lower(s)
        print(S)
        print(x)
        i -= 1