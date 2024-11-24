
def max(a,b):
    if a > b : return a
    else : return b

def test(a):
    cnt = 1
    for i in range(len(a)):
        x = a.count(a[i])
        if x > cnt : 
            cnt = x
            z = a[i]
    print(z)

if __name__ == "__main__":
    a = [1, 2, 2, 3, 3, 3, 4]
    test(a)