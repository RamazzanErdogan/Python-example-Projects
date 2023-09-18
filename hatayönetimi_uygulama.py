def parola_sorgulama(psw):
    türkce_karakterler="şçüğöıİ+%&/()?!'^#${["
    for p in psw:
        if p in türkce_karakterler:
            raise TypeError("LÜTFEN TÜRKÇE KARAKTER ve SEMBOLLER GİRMEYİNİZ.")
         
    print("GEÇERLİ PAROLA")
döngü_değeri=True
while döngü_değeri:
    döngü_değeri=False
    psw=input("ŞİFRE= ")
    try:
        parola_sorgulama(psw)
    except TypeError as eror:
        print(eror)
        döngü_değeri=True
    finally:
        print("**") #Finally bloğu her zaman çalıştırlır bu kodda bir etkisi olmasada görelim...
    if döngü_değeri==False:
        döngü_değeri=False
    