kelime = input("Bir kelime girin: ")
baslangic = int(input("Başlangıç sayısını girin: "))
bitis = int(input("Bitiş sayısını girin: "))
if baslangic > len(kelime):
	print("Başlangıç sayısı kelime uzunluğundan fazla olamaz!")
elif bitis > len(kelime):
	print("Bitiş sayısı kelime uzunluğundan fazla olamaz!")
elif baslangic <= 0 or bitis <= 0:
	print("Başlangıç veya bitiş sayısı 0'dan küçük veya 0 olamaz!")
elif baslangic > bitis:
	print("Başlangıç sayısı bitiş sayısından büyük olamaz!")
else:
	baslangic = baslangic - 1
	cikar = kelime[baslangic:bitis]
	kelime = kelime.replace(cikar,'')
	print("Verilen Kelimenin son hali: " + kelime)