
def test(a):
    lent = 0
    s=str
    for i in a:
        if lent < len(i):
            lent = len(i)
            s=i
    return s
if __name__ == "__main__":
    a=[]
    n=int(input())
    for i in range(n):
        x=str(input())
        a.append(x)
    result = test(a)
    print(result)