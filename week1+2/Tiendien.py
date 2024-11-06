from math import*
if __name__ == '__main__':
    n=int(input())
    if n>=0 and n<=50 :
        sum = n*1678
    elif n>50 and n<101:
        sum = n*1784
    else : 
        sum= n*2014
    print("Số tiền phải trả khi dùng",n,"số điện là",sum)