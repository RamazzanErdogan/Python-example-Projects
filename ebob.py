lis1=[]
lis2=[]
x=int(input("sayı 1:"))
y=int(input("sayı 2:"))
lis1.append(x)
lis1.append(y)
lis1.sort()
print(lis1)
for i in range(2,lis1[0]):
    if x%i==0 and y%i==0:
        lis2.append(i)  
if len(lis2)==0:
        print("BU İKİ SAYI ARALARINDA ASALDIR")
else:
    print(f"EBOB:{max(lis2)}")