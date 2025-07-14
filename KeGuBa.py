import random
pilihan = ["rock", "paper","scissors"]

print('\t=====Game Rock Paper Scissors=====\n\t CTRL+C untuk selesaikan permainan')
print('Masukkan pilihanmu dengan huruf kecil semua!')

while True:
    komputer = random.choice(pilihan)
    pemain = input("pilih salah satu antara rock, paper, scissors: ")
    if pemain == komputer:
        print(f'pilihanmu adalah {pemain}')
        print(f'pilihan komputer adalah {komputer}')
        print('Hasil Seri \n========Try Again========')

    elif pemain == 'rock' and komputer == 'scissors' :
        print(f'pilihanmu adalah {pemain}')
        print(f'pilihan komputer adalah {komputer}')
        print('Kamu Menang!!! \n================Try Again================')
    elif pemain == 'paper' and komputer == 'rock' :
        print(f'pilihanmu adalah {pemain}')
        print(f'pilihan komputer adalah {komputer}')
        print('Kamu Menang!!! \n================Try Again================')
    elif pemain == 'scissors' and komputer == 'paper' :
        print(f'pilihanmu adalah {pemain}')
        print(f'pilihan komputer adalah {komputer}')
        print('Kamu Menang!!! \n================Try Again================')

