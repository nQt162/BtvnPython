
def test(s):
    a=sorted(s)
    b =""
    for i in a:
        b += i
    print(b)

if __name__ == "__main__":
    s= str(input())
    test(s)