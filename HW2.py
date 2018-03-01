import time
a = 1
b = 1
c = int(input("Fibonacci dizisinin kaçıncı değere kadar yazdırılacağını giriniz: "))
i = 2
while i<=c+1:
	a_eski = a
	b_eski = b
	a = b_eski
	b = a_eski + b_eski
	print (b)
	i += 1
print("10 sn sonra çıkış yapılacaktır..")
time.sleep(10)