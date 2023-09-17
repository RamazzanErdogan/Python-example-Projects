# Basamak Sayısı Bulma 
x=int(input("Lütfen bir sayı degeri Giriniz:"))
sayac=1
while x>=10:
    x=x/10
    sayac=sayac+1
print(sayac)