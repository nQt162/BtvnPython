
def test(s1,s2):
    if len(s1) != len(s2) : return 0
    else :
         a = sorted(s1)
         b = sorted(s2)
         for i in range(len(a)):
              if a[i] != b[i] :
                   return 0
                   break
    return 1

if __name__ == "__main__":
     s1 = str(input())
     s2 = str(input())
     if test(s1,s2)  : print("TRUE")
     else : print("FALSE")