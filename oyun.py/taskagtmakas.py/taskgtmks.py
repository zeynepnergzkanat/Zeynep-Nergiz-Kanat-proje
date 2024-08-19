import random

def tas_kagit_makas_ZEYNEP_NERGİZ_KANAT():
    secenek = ["taş", "kağıt", "makas"]
    taş = secenek[0]
    kağıt = secenek[1]
    makas = secenek[2]

    oyuncu_galibiyetleri = 0
    bilgisayar_galibiyetleri = 0

    print("Taş, Kağıt, Makas Oyununa Hoşgeldiniz!\n")

    print("Oyun, ilk iki turu kazanan tarafın galip geldiği bir oyundur.\n")

    print("Taş, Kağıt, Makas seçeneklerinden birini seçerek oynayabilirsiniz.\n")

    print("Oyunda taş makası, makas kağıdı, kağıt da taşı yener.\n")

    print("Oyundan çıkmak isterseniz, lütfen 'q' tuşuna basınız.\n")

    while True:

        while oyuncu_galibiyetleri < 2 and bilgisayar_galibiyetleri < 2:
            secim = input("Taş mı? Kağıt mı? Makas mı? ").lower()

            if secim == 'q':
                print("Oyundan ayrılıyorsunuz...")
                return

            if secim not in secenek:
                print("Geçersiz bir seçim yaptınız, lütfen tekrar seçim yapın.")
                continue

            bil_secim = random.choice(secenek)
            if secim == taş:
                if bil_secim == taş:
                    print("Bilgisayar taşı seçti\nSonuç: Berabere")
                elif bil_secim == kağıt:
                    print("Bilgisayar kağıdı seçti\nSonuç: Kaybettiniz")
                    bilgisayar_galibiyetleri += 1
                else:
                    print("Bilgisayar makası seçti\nSonuç: Kazandınız")
                    oyuncu_galibiyetleri += 1

            elif secim == kağıt:
                if bil_secim == taş:
                    print("Bilgisayar taşı seçti\nSonuç: Kazandınız")
                    oyuncu_galibiyetleri += 1
                elif bil_secim == kağıt:
                    print("Bilgisayar kağıdı seçti\nSonuç: Berabere")
                else:
                    print("Bilgisayar makası seçti\nSonuç: Kaybettiniz")
                    bilgisayar_galibiyetleri += 1

            elif secim == makas:
                if bil_secim == taş:
                    print("Bilgisayar taşı seçti\nSonuç: Kaybettiniz")
                    bilgisayar_galibiyetleri += 1
                elif bil_secim == kağıt:
                    print("Bilgisayar kağıdı seçti\nSonuç: Kazandınız")
                    oyuncu_galibiyetleri += 1
                else:
                    print("Bilgisayar makası seçti\nSonuç: Berabere")

            print(f"Skor: Oyuncu {oyuncu_galibiyetleri} - Bilgisayar {bilgisayar_galibiyetleri}")

        if oyuncu_galibiyetleri == 2:
            print("Tebrik ederim, oyunu siz kazandınız!")
        else:
            print("Üzgünüm, oyunu kaybettiniz.")

        # Yeni oyun
        yeni_oyun = input("Bir oyun daha oynamak ister misiniz? (evet/hayır): ").lower()
        bilgisayar_istek = random.choice(['evet', 'hayır'])

        if yeni_oyun != 'evet' or bilgisayar_istek != 'evet':
            print("Oyun sona erdi, oynadığınız için teşekkürler.")
            break
        else:
            print("Yeni oyun başlıyor.")
            # Tur sayacı sıfırlanıyor
            oyuncu_galibiyetleri = 0
            bilgisayar_galibiyetleri = 0

tas_kagit_makas_ZEYNEP_NERGİZ_KANAT()
