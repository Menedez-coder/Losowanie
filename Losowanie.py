import random
#otwieramy plik
plik = open("lista.txt", "r")
try:
    dane = plik.read()
    nazwiska = dane.split() #tekst jest podzielony na nazwiska)

finally:
    plik.close()
spacja = ("          ")
wylosowane = random.sample(nazwiska, len(nazwiska))

for i in range(len(nazwiska)):
     if wylosowane[i]==nazwiska[i]:
         a= (i+1)%len(nazwiska) # %len(nazwiska) zapewnia przy zmianie indeksow ze jak jestesmy na koncu to wrocimy na poczatek ?r?d?o https://stackoverflow.com/questions/2493920/how-to-switch-position-of-two-items-in-a-python-list
         wylosowane[i], wylosowane[a] = wylosowane[a], wylosowane[i] # swap.index tu uzyte


for i in range(len(nazwiska)):
    f = open("wyniki.txt","w")
    with open("wyniki.txt","a") as plik_wynik:
        for i in range(len(nazwiska)):
            linia = nazwiska[i] + spacja + wylosowane[i] + "\n"
            plik_wynik.write(linia)
print("Wyniki zapisane w pliku wyniki.txt!")
#?r?d?a pomocowe to https://www.w3schools.com/python/python_file_write.asp i
plik.close()