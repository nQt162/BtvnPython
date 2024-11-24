
def test(a,b):
    c = []
    for i in range(len(a)):
        if a[i] in b : c.append(a[i])
    print(c) 

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    b = [3, 4, 5, 6]
    test(a,b)