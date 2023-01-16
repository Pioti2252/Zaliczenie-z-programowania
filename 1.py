import random
from random import randint
import os
from time import sleep
import sys

kw=1000
kwt=1000

#gui
print("Masz 18 lat ? T/N")
z=input().lower()
if z.lower()=="t":
    print("Możesz grać")
    sleep(1.0)
else:
    print ("Dowidzenia")
    sys.exit(0)

while True:
    print("Prosze wybrać grę w którą chcesz zagrać")
    sleep(1.0)
    print("1. Ruletka")
    sleep(1.0)
    print("2. Zgadnij liczbę")
    sleep(1.0)
    print("3. Rosyjska Ruletka")
    sleep(1.0)
    print("4. Kółko i krzyżyk")
    sleep(1.0)
    print("5. wyjście")

    try:
        x = int(input("W co masz ochote zagrać: "))
    except ValueError:
        print("Podaj liczbe")
        continue
        
        #game1
    if x==1:
        def sprawdz_czy_wygral(obstawienie, wynik):
            if (wynik % 2 == 0 and obstawienie == "czerwone") or (wynik % 2 == 1 and obstawienie == "czarne"):
                return True
            elif wynik == 0 and obstawienie == "zielone":
                return True
            else:
                return False

        print("Witaj w ruletce. Twoja wygrana zależy od wylosowanej liczby. Liczby nieparzyste to kolor czarny, liczby parzyste to kolor czerwony, a liczba 1 to kolor zielony.")
        sleep(1.0)
        print("Mnożniki:")
        sleep(1.0)
        print("- Czarne: 2x")
        sleep(1.0)
        print("- Czerwone: 2x")
        sleep(1.0)
        print("- Zielone: 10x")

        mnozniki = {
            "czarne": 2,
            "czerwone": 2,
            "zielone": 10,
        }

        while True:
            sleep(1.0)
            print(f"Masz {kw} PLN.")
            
            try:
                sleep(1.0)
                c = float(input("Ile chcesz obstawić PLN: "))
            except ValueError:
                print("Podaj liczbe")
                continue
            
            if c > kw:
                print("Nie masz wystarczająco środków.")
                continue
            print("Na co chcesz obstawić (czarne, czerwone, zielone)?")
            obstawienie = input().lower()
            
            if obstawienie not in mnozniki:
                print("Nieprawidłowe obstawienie.")
                continue
            
            wynik = random.randint(0, 36)
            
            if sprawdz_czy_wygral(obstawienie, wynik):
                print("Gratulacje, wygrałeś!")
                sleep(1.0)
                kw += c * mnozniki[obstawienie]
            else:
                print("Niestety, przegrałeś.")
                sleep(1.0)
                kw -= c
            
            if kw <= 0:
                print("Nie masz już środków na koncie. Koniec gry.")
                sleep(1.0)
                break
            
            print("Czy chcesz kontynuować grę (T/N)?")
            if input().upper() == "N":
                sleep(1.0)
                break

        #game2
    elif x==2:
        print("Wybrałeś/aś zgadnij liczbę. Twoja wygrana zalezy od tego czy zgadniesz liczbę, którą wylosuje komputer.")
        sleep(1.0)

        while True:
            print(f"Masz {kwt} PLN.")
            sleep(1.0)
            print("Ile chcesz obstawić PLN")
            sleep(1.0)
            p = int(input())

            if p > kwt:
                print("nie masz wystarczająco środków")
                sleep(1.0)
                continue

            wylosowana_liczba = random.randrange(1, 11)

            print("Wybierz jedną liczbę z zakresu 1-11")
            sleep(1.0)
            obstawiona_liczba = input()

            if obstawiona_liczba == wylosowana_liczba:
                print("Gratulacje wygrałeś")
                sleep(1.0)
                kwt += p * 2
            else:
                print("Niestety, przegrałeś")
                sleep(1.0)
                kwt -= p

            if kwt <= 0:
                print("Nie masz już środków na koncie. Koniec gry.")
                sleep(1.0)
                break

            print("Chcesz grać dalej (T/N)?")
            if input().upper() == "N":
                sleep(1.0)
                break
            
        #game3
    elif x==3:
        hajs = 1000
        i = 1 
        tempm = 0 
        hajs2 = 0 

        def shot_save():
            global hajs,i,tempm,hajs2 
            i = i *2 
            print("PIF")
            sleep(0.5)
            print("PAF")
            sleep(0.5)
            hajs2 = hajs - stawka 
            tempm0 = stawka * i 
            tempm = (stawka * i) + hajs2 
            print("ALIVEEEE Do you take: ", tempm0, "PLN")
            sleep(1.0)

        def shot_die(): 
            global hajs,stawka,i,hajs2,tempm 
            i, hajs2, tempm = 1, 0, 0 
            print("PIF")
            sleep(0.5)
            print("PAF")
            sleep(0.5)
            print("DIEEEEEEEE HA! HA! HA! HA!") 
            sleep(1.0) 
            hajs = hajs - stawka 

        def los():
            global kr,pr
            kr = randint(1,3)
            pr = randint(1,3)

        def krnotpr():
            global kr,pr,still
            if kr != pr: 
                shot_save() 
                still = int(input("0-Take 1-Shot: ")) 

        print("| Witam w rosyjskiej ruletce! | | Każdy strzał to 30% na śmierć | | Za każdym strzałem możesz wygrać 2 razy więcej!!! |")
        sleep(1.0)
   
        while True:
          print("Stan konta: ",hajs,"PLN")
          sleep(1.0)
          stawka = int(input("Za ile PLN grasz: "))
          sleep(1.0)
          if stawka>0 and stawka<=hajs:
            still=int(input("1-Shot or 2-Exit: "))
            if still == 2:
             break
            while still==1:
             los()
             krnotpr()
             if kr==pr:
                shot_die()
                break
             if still==0:
              hajs=hajs2+tempm
              break
             elif hajs<=0:
                print("Brak środków do gry")
                break
        #game4
    elif x==4:
        tablica = [["_" for i in range(3)] for j in range(3)]

        def wyd_tablica():
            for wiersz in tablica:
                print(" ".join(wiersz))

        def ruch(gracz, wiersz, kolumna):
            if wiersz in range(3) and kolumna in range(3) and tablica[wiersz][kolumna] == "_":
                tablica[wiersz][kolumna] = gracz
                return True
            else:
                return False

        def sprawdz_wygrana(gracz):
            for i in range(3):
                if tablica[i] == [gracz, gracz, gracz]:
                    return True
            for i in range(3):
                if tablica[0][i] == gracz and tablica[1][i] == gracz and tablica[2][i] == gracz:
                    return True
            if tablica[0][0] == gracz and tablica[1][1] == gracz and tablica[2][2] == gracz:
                return True
            if tablica[0][2] == gracz and tablica[1][1] == gracz and tablica[2][0] == gracz:
                return True
            return False


        obecny_gracz = "X"
        while True:
            wyd_tablica()
            wiersz = int(input("Wprowadź wiersz (0, 1, 2): "))
            kolumna = int(input("Wprowadź kolumnę (0, 1, 2): "))
            if ruch(obecny_gracz, wiersz, kolumna):
                if sprawdz_wygrana(obecny_gracz):
                    print(f"Gracz {obecny_gracz} wygrał!")
                    sleep(1.0)
                    break
                obecny_gracz = "X" if obecny_gracz == "O" else "O"
            else:
                print("Nieprawidłowy ruch!")
    elif x==5:
         sys.exit(0)          
    else:
        print("Nie ma takiej gry")

    

