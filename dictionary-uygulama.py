# Kullanıcıdan alınan bilgileri dictionary sözlük içersine saklayınız
ögrenciler={}
x=int(input("Kaç öğrenci bilgisini Dictionary sözlük içersine saklamak istiyorsunuz==\n"))
i=0
while i<x:
        numara=input("Numaranızı giriniz=")
        ad=input("Adınızı giriniz=")
        soyad=input("Soyadınız girniz=")
        tel=input("TEL=")
        ögrenciler.update({numara:{"AD":ad,"Soyad":soyad,"TEL":tel}})
        i+=1
# Öğrenci numarasını kullanıcıdan alıp öğrenci bilgilerini gösterin
ogrno=input("Aramak istediğiniz öğrenci numarası giriniz= ")
print(ögrenciler[ogrno])
