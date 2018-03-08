kelime = input("Bir kelime veya cümle giriniz: ")
duzenli = ""
for harf in kelime:
    if harf not in duzenli:
        duzenli += harf
print("Kelime veya cümleden tekrarlanan harfler kaldırıldı!\nKelime veya cümlenin düzenlenmiş hali: " + duzenli)
