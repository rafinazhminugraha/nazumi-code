"""numbers = []
count = 0

while count < 3:
    number = float(input("Masukkan bilangan: "))

    if not numbers or number < min(numbers):
        numbers.append(number)
        count = 0
    else:
        count += 1

hasil_kali = 1
for num in numbers:
    hasil_kali *= num

    print("Hasil kali dari bilangan yang lebih kecil dari sebelumnya:", hasil_kali)"""

banyakBilangan = int(input('Masukkan banyak bilangan: '))
bilanganBukanPrima = 0
for i in range(0, banyakBilangan):
    bilangan = int(input(f'Masukkan bilangan ke-{i+1}: '))

    prima = True 
    for i in range(2, bilangan): 
        if (bilangan % i == 0): 
            prima = False 
            break 
    if prima == False:
        bilanganBukanPrima += bilangan

print(f'Hasil penjumlahan bilangan yang bukan prima: {bilanganBukanPrima}')