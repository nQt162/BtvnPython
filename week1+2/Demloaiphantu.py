if __name__ == '__main__':
    # cho sau a có 3 số nguyên, 5 số thực, 2 xâu ký tự
    a=[1, 2, 3, "Python", "c++", 1.54, 3.45, 4.56, 6.78, 8.77]
    songuyen=sothuc=xaukytu=0
    for i in range(0, len(a)):
        if type(a[i]) is int : songuyen+=1
        elif type(a[i]) is float : sothuc+=1
        else : xaukytu+=1
    print(songuyen,sothuc,xaukytu)
