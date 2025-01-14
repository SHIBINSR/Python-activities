    #confusion in electricity bill

tu=int(input("enter the total unit:"))
if tu<=50:
    pr=tu*0.50
    per=pr*0.20
    tp=pr+per
    print(int(tp))
elif tu<=150:
    pr=(50*.50)+tu-100*.75
    per=pr*.20
    tp=pr+per
    print(int(tp))
elif tu<=250:
    pr=(50*.50)+(100*.75)+tu-100*1.20
    per = pr * .20
    tp = pr + per
    print(int(tp))
elif tu>250:
    pr=(50*.50)+(100*.75)+(100*1.20)+tu-250*1.50
    per = pr * .20
    tp = pr + per
    print(int(tp))
