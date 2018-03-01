# -*- coding: utf-8 -*-
import sys
import os
import time

yesil = "\033[32m"
kirmizi = "\033[91m"
sifirla = "\033[0m"
os.system('cls')
for x in range(0,100):
	islem = input(print(yesil+"[1]"+sifirla+"Toplama\n"+yesil+"[2]"+sifirla+"Çıkarma\n"+yesil+"[3]"+sifirla+"Çarpma\n"+yesil+"[4]"+sifirla+"Bölme\n"+yesil+"[5]"+sifirla+"Çıkış\nLütfen bir seçim yapın: "))
	if islem == "1":
		os.system('cls')
		sayi1 = int(input("Birinci sayıyı girin: "))
		sayi2 = int(input("İkinci sayıyı girin: "))
		sonuc = sayi1 + sayi2
		print(yesil + "İşlem başarılı!" + sifirla)
		time.sleep(0.5)
		print("Sonuç:",sonuc)
		time.sleep(2)
		os.system('cls')
	elif islem == "2":
		os.system('cls')
		sayi1 = int(input("Birinci sayıyı girin: "))
		sayi2 = int(input("İkinci sayıyı girin: "))
		sonuc = sayi1 - sayi2
		print(yesil + "İşlem başarılı!" + sifirla)
		time.sleep(0.5)
		print("Sonuç:",sonuc)
		time.sleep(2)
		os.system('cls')
	elif islem == "3":
		os.system('cls')
		sayi1 = int(input("Birinci sayıyı girin: "))
		sayi2 = int(input("İkinci sayıyı girin: "))
		sonuc = sayi1 * sayi2
		print(yesil + "İşlem başarılı!" + sifirla)
		time.sleep(0.5)
		print("Sonuç:",sonuc)
		time.sleep(2)
		os.system('cls')
	elif islem == "4":
		os.system('cls')
		sayi1 = int(input("Birinci sayıyı girin: "))
		sayi2 = int(input("İkinci sayıyı girin: "))
		try:
			sonuc = sayi1 / sayi2
		except ZeroDivisionError:
			sonuc = 0
		print(yesil + "İşlem başarılı!" + sifirla)
		time.sleep(0.5)
		print("Sonuç:",sonuc)
		time.sleep(2)
		os.system('cls')
	elif islem == "5":
		os.system('cls')
		print(kirmizi + "Çıkış yapılıyor..." + sifirla)
		time.sleep(0.7)
		sys.exit()
	else:
		print(kirmizi + "Bilinmeyen bir seçim yaptınız çıkış yapılıyor.." + sifirla)
		time.sleep(0.3)
		sys.exit()
x+=1