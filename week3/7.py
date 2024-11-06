def test(a):
    if a<0: print("Giá trị tuyệt đối: ",a*-1)
    else: print("Giá trị tuyệt đối: ",a)

if __name__ == '__main__':
    a=int(input())
    test(a)