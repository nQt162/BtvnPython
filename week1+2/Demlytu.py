if __name__ == '__main__':
    s=input()
    chuso=0
    chucai=0
    for i in range(0,len(s),1):
        if(s[i].isdigit() ): chuso+=1
        elif (s[i].isalpha() ): chucai+=1
    print("Số ký tự chữ:",chucai)
    print("Số ký tự số:",chuso)
