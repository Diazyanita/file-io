#file_pantun = open("pantun.txt", "r")

#pantun = file_pantun.readlines ()

#print (pantun[0])

#print (pantun[2])

#file_pantun.close

file_pantun = open("pantun.txt", "r")

pantun = file_pantun.readlines ()

for teks in pantun:
    print (teks)

    file_pantun.close ()