import random
pilihan = ["rock", "paper","scissors"]

print('\t=====Game Rock Paper Scissors=====\n\t CTRL+C untuk selesaikan permainan')
print('Masukkan pilihanmu dengan huruf kecil semua!')

while True:
    komputer = random.choice(pilihan)
    pemain = input("pilih salah satu antara rock, paper, scissors: ")
