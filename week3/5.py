def test(a):
    if a%4==0 and a%100!=0: print("Năm nhuận")
    elif a%400==0 : print("Năm nhuận")
    else : print("Không phải là năm nhuận")
if __name__ == '__main__':
    a=int(input())
    test(a)