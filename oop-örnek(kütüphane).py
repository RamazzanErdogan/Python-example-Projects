class Kitaplar:
    stoksayısı=1
    def __init__(self,kitapadi):
        self.kitapadi=kitapadi

    def bilgiler(self):
        if self.kitapadi=="A":
            print(f"{self.kitapadi}'Kitabı HAKKINDA UZUN UZUN BİLGİLER ÖRNEĞİN YAYIN TARİHİ,YAZARI VS")
            al=input("KİTABI ALMAK İSTİYORMUSUNUZ: ")
            stoksayısı=0
            if al.upper()=="E":
                 if stoksayısı<=0:
                     print("MAALESEF BU ÜRÜN STOKLARDA MEVCUT DEĞİLDİR")
                 else:
                     stoksayısı-=1
        if self.kitapadi=="B":
            print(f"{self.kitapadi}'Kitabı HAKKINDA UZUN UZUN BİLGİLER ÖRNEĞİN YAYIN TARİHİ,YAZARI VS")
            al=input("KİTABI ALMAK İSTİYORMUSUNUZ: ")
            stoksayısı=3
            if al.upper()=="E":
                 if stoksayısı<=0:
                     print("MAALESEF BU ÜRÜN STOKLARDA MEVCUT DEĞİLDİR")
                 else:
                     stoksayısı-=1
        if self.kitapadi=="C":
            print(f"{self.kitapadi}'Kitabı HAKKINDA UZUN UZUN BİLGİLER ÖRNEĞİN YAYIN TARİHİ,YAZARI VS")
            al=input("KİTABI ALMAK İSTİYORMUSUNUZ: ")
            stoksayısı=5
            if al.upper()=="E":
                 if stoksayısı<=0:
                     print("MAALESEF BU ÜRÜN STOKLARDA MEVCUT DEĞİLDİR")
                 else:
                     stoksayısı-=1
        if self.kitapadi=="D":
            print(f"{self.kitapadi}'Kitabı HAKKINDA UZUN UZUN BİLGİLER ÖRNEĞİN YAYIN TARİHİ,YAZARI VS")
            al=input("KİTABI ALMAK İSTİYORMUSUNUZ: ")
            stoksayısı=0
            if al.upper()=="E":
                 if stoksayısı<=0:
                     print("MAALESEF BU ÜRÜN STOKLARDA MEVCUT DEĞİLDİR")
                 else:
                     stoksayısı-=1
        if self.kitapadi=="E":
            print(f"{self.kitapadi}'Kitabı HAKKINDA UZUN UZUN BİLGİLER ÖRNEĞİN YAYIN TARİHİ,YAZARI VS")
            al=input("KİTABI ALMAK İSTİYORMUSUNUZ: ")
            stoksayısı=1
            if al.upper()=="E":
                 if stoksayısı<=0:
                     print("MAALESEF BU ÜRÜN STOKLARDA MEVCUT DEĞİLDİR")
                 else:
                     stoksayısı-=1
        else:
            print("ARADIĞINIZ KİTAP KÜTÜPHANE SİSTEMİMİZDE BULUNMAMMAKTADIR")
        
x=input("KİTAP ADINI GİRİNİZ:")
p1=Kitaplar(x.upper())
p1.bilgiler()