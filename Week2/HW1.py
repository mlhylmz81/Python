import random
toplam = 0
arr = [None] * 100
for i in range(1, 100):
	arr[i] = i
	arr[0] = random.randint(1, 99)
	toplam = toplam + arr[i]
toplam += arr[0]
print("Liste: \n",arr,"\n")
random.shuffle(arr)
TekrarlananSayi = toplam - 4950
print("Tekrarlanan sayı: ",TekrarlananSayi)