def check1(a):
        if a%2==0 and a>=0 : return 1
        else: return 0
def check2(a):
        if a>0 : print("Dương")
        elif a<0: print("ÂM")
        else : print("Số 0")
if __name__=='__main__':
        a=int(input())
        if check1(a) : print("Chẵn")
        else: print("Lẻ")
        check2(a)