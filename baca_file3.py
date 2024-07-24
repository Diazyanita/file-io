file_pantun = open("pantun.txt", "r")

pantun = file_pantun.readlines ()

for teks in pantun:
    print (teks)

    file_pantun.close ()