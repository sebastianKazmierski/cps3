def funkcja_abominujaca(krok):
    ile_mnozyc = 0
    temp = krok
    while temp < 1:
        temp *= 10
        ile_mnozyc += 1

    return krok, ile_mnozyc


def get_arguments(start: float, step: float, length: int):
    krotki_z_krokami = list(map(funkcja_abominujaca, [step]))
    krotka_z_poczatkiem = funkcja_abominujaca(start)

    for krok in krotki_z_krokami:
        mnoznik = 10 ** max(krok[1], krotka_z_poczatkiem[1])
        wartosci = [(krotka_z_poczatkiem[0] * mnoznik + krok[0] * mnoznik * x) / mnoznik for x in range (length + 1)]
        print(wartosci)

