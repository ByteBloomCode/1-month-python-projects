print('çarpma için . , bölme için / , toplama için + , çıkarma için - işaretini giriniz')

x=float(input('1. sayıyı giriniz:'))
işlem=input('işlemi giriniz:')
y=float(input('2. sayıyı giriniz:'))

if işlem=='.':
    çarpma=float(x)*float(y)
    print('Çarpma:',çarpma)

if işlem=='/':
    if x==0 and y==0:
        print('belirsiz')
    elif y==0:
        print('tanımsız')
    else:
        bölme=x/y
        print('Bölme:',bölme)    
   
    
        


if işlem=='+':
    toplama=float(x)+float(y)
    print('Toplama:',toplama)

if işlem=='-':
    çıkarma=float(x)-float(y)
    print('Çıkarma:',çıkarma)               




