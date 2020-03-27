def funkcja_abominujaca(krok):
    ile_mnozyc = 0
    temp = krok
    while temp < 1:
        temp *= 10
        ile_mnozyc += 1

    return krok, ile_mnozyc


if __name__ == "__main__":
    krotki_z_krokami = list(map(funkcja_abominujaca, [.00001, .0001, .001, .01, .1, 1, 10]))
    krotka_z_poczatkiem = funkcja_abominujaca(.1)
    liczba_krokow = 13

    for krok in krotki_z_krokami:
        mnoznik = 10 ** max(krok[1], krotka_z_poczatkiem[1])
        wartosci = [(krotka_z_poczatkiem[0] * mnoznik + krok[0] * mnoznik * x) / mnoznik for x in range (liczba_krokow + 1)]
        print(wartosci)