
nomi = open("/home/exit/Documents/Programs/MyPrograms/Wordlist/nomi").read().splitlines()
count_01=0
count=0
data=1950
with open ('ita.txt', 'a') as f:
    while count_01 <= 9:
        for name in nomi:
            f.write (name + "0" + str(count_01) + "\n")
            f.write (name.upper() + "0" + str(count_01) + "\n")
            f.write (name.title() + "0" + str(count_01) + "\n")
        count_01 += 1
    while count <= 99:
        for name in nomi:
            f.write (name + str(count) + "\n")
            f.write (name.upper() + str(count) + "\n")
            f.write (name.title() + str(count) + "\n")
        count += 1
    while data <= 2023:
        for name in nomi:
            f.write (name + str(data) + "\n")
            f.write (name.upper() + str(data) + "\n")
            f.write (name.title() + str(data) + "\n")
        data += 1

    