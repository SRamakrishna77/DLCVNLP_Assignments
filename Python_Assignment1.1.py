def division7_not5():
    a=1999
    b=3201
    c=[]
    for i in range(a,b):
        if(i%7==0 and i%5 != 0):
            c.append(i)
        # else:
        #     print("No Such values exist")
    return c


c = division7_not5()
print(c)
print(len(c))


