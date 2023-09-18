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