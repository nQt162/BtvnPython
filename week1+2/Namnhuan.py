from math import*
if __name__ == "__main__" :
    n=int(input())
    if (n%4==0) and (n%100!=0):
        print(n,"Là năm nhuận")
    elif n%400 ==0 :
        print(n,"Là năm nhuận")
