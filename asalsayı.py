# İf-else koşullu ifadeleri ve for döngüsüs ile asal sayı bulma 
x=int(input("ASAL OLUP OLMADIĞINI ÖĞRENMEK İSTEDİĞİNİZ SAYIYI GİRİNİZ==.."))
if x==1:
    print("SAYI ASAL DEĞİLDİR.")
for i in range(2,x):
    y=x%i
    print(y)
    if(y==0):
        koşul=True
        break
    else:
        koşul=False
if koşul:
    print("sayı asal değil ")
else:
    print("sayı asal ")
