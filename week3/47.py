
def test(s):
    a = list(set(s))
    return a
#hello

if __name__ == "__main__":
    s=[1, 2, 3, 3, 4, 4, 5]
    a= test(s)
    print(a)
