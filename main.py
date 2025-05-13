import math

while True:
    try:
        sayi = float(input("Bir sayı girin: "))
        assert sayi >= 0
        print("Sonuç:", math.sqrt(sayi))
        break
    except:
        print("Pozitif bir sayı girin!")
