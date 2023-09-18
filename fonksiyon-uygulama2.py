def islem(islemadi):
    def toplama(sayilar):
        toplam=0
        for i in sayilar:
            toplam+=i
            
        return toplam
    def carpma(sayilar):
        carpım=1
        for i in sayilar:
            carpım=i*carpım
        return carpım 
    if islemadi=="TOPLAMA":
        return toplama
    else:
        return carpma
islem_adi=input("YAPMAK İSTEDİĞİNİZ İŞLEM: \n 1-TOPLAMA \n2-ÇARPMA \n==>").upper()   
sayi_adedi=int(input("KAÇ ADET SAYI DEĞERİ GİRMEK İSTİYORSUNUZ:"))
a=0
sayilar=()
while a<sayi_adedi:
    sayi=int(input("SAYI:"))
    sayilar+=(sayi,)
    a+=1
print(islem(islem_adi)(sayilar))
