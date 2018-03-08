kelime = input("Bir kelime girin: ")
Duz = []
Ters = []
for i in kelime:
    Duz.append(i) 
uzunluk = len(kelime)
for x in range(0, uzunluk):
    Duz.append(Duz[x])
TersIndex = uzunluk
TersIndex = TersIndex - 1
while(TersIndex >= 0):
    Ters.append(Duz[TersIndex])
    TersIndex = TersIndex - 1
dogru = 0
for j in range(0, uzunluk):
        if Duz[j] == Ters[j]:
                dogru = dogru + 1        
if dogru == uzunluk:
        print("Girilen kelime Palindromdur.")
else:
        print("Girilen kelime Palindrom degildir.")