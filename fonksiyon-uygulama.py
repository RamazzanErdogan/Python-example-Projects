# Göndeerilen kelimeyi belirtilen kez ekranda yazan kod yazınız.
# def tekraredenkelimefonk(kelime):
    # a=0
    # while a<x:
        # print(f"{kelime}")
        # a+=1
# kelime=input("TEKRAR ETMESİNİ İSTEDİĞİNİZ KELİMEYİ GİRİNİZ= ")
# x=int(input("TEKRAR SAYISINI GİRİNİZ="))
# tekraredenkelimefonk(kelime)
# 
# Kullanıcıdan Kendine gönderilen sınırsız sayıda parametreyi listeye çeviren bir kod yazınız.
# def sinirsizlisteyapma(*listeelmanları):
    # print(list(listeelmanları))
    # 
    # 
# sinirsizkelime=input("LİSTELEMEK İSTEDİĞİNİZ KELİMELERİ GİREBİLİRİSİNİZ(parametreleri virgülle ayırarak giriniz)= \n")
# listeelmanları=sinirsizkelime.split(",")
# sinirsizlisteyapma(listeelmanları)

# Gönderilen iki sayı arasındaki tüm asal sayıları bulunuz.

# def asal_sayi_bulma(baslangic, bitis):
#     for i in range(baslangic, bitis):
#         if i > 1:
#             for j in range(2, i):
#                 if (i % j) == 0:
#                     break
#             else:
#                 print(i)

# baslangic = int(input("baslangic degerini giriniz: "))
# bitis = int(input("bitis degerini giriniz: "))
# asal_sayi_bulma(baslangic, bitis)

# Kendisine gönderilen sayının tam bölenlerini listeleyen bir kod yazınız.
def tam_bölen_bul(sayi):
    tam_bolenler_listesi=[]
    for x in range(2,sayi):
        if sayi%x==0:
            tam_bolenler_listesi.append(x)
    if tam_bolenler_listesi==[]:
        print("Bu sayı Asal sayıdır")
    else:
        print(tam_bolenler_listesi)
sayi=int(input("BİR SAYI DEGERI GIRNIZ="))
tam_bölen_bul(sayi)