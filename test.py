def fun(s):
    cvar=s[0]
    dvar=s[0]
    count=1
    s=""
    i=1
    end=len(s)-1
    while(i<end):
        dvar=s[i]
        if dvar==cvar:
            count+=1
            i=i+1
        else:
            s=s+cvar+str(count)
            cvar=dvar
            count=1
            i=i+1
   
    return s

print(fun("aaab"))