for satir in range(7):
    for sutun in range(9):
        if (satir==0 and (sutun==2 or sutun==6)):
            print("*",end="")
        elif(satir==1 and (sutun==1 or sutun==2 or sutun==3 or sutun==5 or sutun==6 or sutun==7)):
            print("*",end="")
        elif(satir==2 and (sutun>=0 and sutun<=8)):
            print("*",end="")
        elif(satir==3 and (sutun>=1 and sutun<=7)):
            print("*",end="")
        elif(satir==4 and (sutun>=2 and sutun<=6)):
            print("*",end="")
        elif(satir==5 and (sutun>=3 and sutun<=5)):
            print("*",end="")
        elif(satir==6 and (sutun==4)):
            print("*",end="")
        else:
            print(" ",end="")
    print()