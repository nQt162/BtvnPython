def check(a):
    if a>=8.0 : print("Giỏi")
    elif 7.0<=a<8.0: print("Khá")
    elif 6.0<=a<7.0: print("Trung bình")
    else : print("Yếu")

if __name__ == '__main__':
    a = float(input())
    check(a)