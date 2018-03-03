# -*- coding: utf-8 -*-
while True:
	islem = input("[+]Toplama\n[-]Çıkarma\n[*]Çarpma\n[/]Bölme\nLütfen yapacağınız işlemi giriniz(Çıkış için exit yazabilirsiniz): ")
	if islem == "exit":
		print("Çıkış yapılıyor...")
		break
	sayi1 = int(input("Birinci sayıyı girin: "))
	sayi2 = int(input("İkinci sayıyı girin: "))
	if islem == "+":
		sonuc = sayi1 + sayi2
	elif islem == "-":
		sonuc = sayi1 - sayi2
	elif islem == "*":
		sonuc = sayi1 * sayi2
	elif islem == "/":
		if sayi2 <= 0:
			sonuc = 0
		else:
			sonuc = sayi1 / sayi2
	print("İşlem başarılı!")
	print("Sonuç:",sonuc)
