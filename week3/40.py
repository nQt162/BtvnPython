
def test(a):
    x = sorted(a)
    y = []
    for i in range (len(a)-1, -1, -1):
        y.append(x[i])
    print(y)


if __name__ == "__main__":
    a = [4, 2, 9, 1]
    test(a)