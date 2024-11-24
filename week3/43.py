
def test(s):
    sum = 0
    for i in s:
        sum += int(i)
    return sum

if __name__ == "__main__":
    s=[1,2,3,4]
    print(test(s))
    