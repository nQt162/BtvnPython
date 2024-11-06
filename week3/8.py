def check1(b):
    if b%4==0 and b%100!=0: return 1
    elif b%400==0 : return 1
    else : return 0

def test(a,b):
    if check1(b):
        if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12: print("Tháng",a,"năm",b,"có 31 ngày")
        elif a==4 or a==6 or a==9 or a==11:  print("Tháng",a,"năm",b,"có 30 ngày")
        elif  a==2: print("Tháng",a,"năm",b,"có 29 ngày") 
    if check1(b)==0:
        if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12: print("Tháng",a,"năm",b,"có 31 ngày")
        elif a==4 or a==6 or a==9 or a==11:  print("Tháng",a,"năm",b,"có 30 ngày")
        elif  a==2: print("Tháng",a,"năm",b,"có 28 ngày")

if __name__ == '__main__':
    a=int(input("Tháng:"))
    b=int(input("Năm:"))
    test(a,b)
