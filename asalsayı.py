# İf-else koşullu ifadeleri ve for döngüsüs ile asal sayı bulma 
x=int(input("ASAL OLUP OLMADIĞINI ÖĞRENMEK İSTEDİĞİNİZ SAYIYI GİRİNİZ==.."))
if x==1:
    print("SAYI ASAL DEĞİLDİR.")
for i in range(2,x):
    
    if(x%i==0):
        koşul=False
        break
koşul=True
if koşul:
    print("sayı asal ")
else:
    print("sayı asal değil")
