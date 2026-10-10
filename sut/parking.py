"""Opłata za postój na parkingu uczelnianym."""
import math

BEZPLATNE_MIN = 15        # tyle minut postoju nic nie kosztuje
LIMIT_GODZINOWY = 180     # do tylu minut liczy się stawkę godzinową
STAWKA_ZA_GODZINE = 5.0   # zł za każdą rozpoczętą godzinę
OPLATA_DOBOWA = 20.0      # zł za postój dłuższy niż 180 minut
MAKS_MINUT = 1440         # jedna doba


def oplata_parkingowa(minuty):
    """Zwraca opłatę w zł za postój trwający `minuty` minut.

    Wymagania: SPECYFIKACJA.md, punkty PK-1 ... PK-5.
    """
    if isinstance(minuty, bool) or not isinstance(minuty, int):
        raise TypeError("czas postoju musi być liczbą całkowitą")
    if minuty < 0 or minuty > MAKS_MINUT:
        raise ValueError("czas postoju musi być z zakresu 0-1440")
    if minuty == 0:
        return 0.0                      # brak postoju
    if 1 < minuty <= BEZPLATNE_MIN:
        return 0.0                      # czas bezpłatny
    if minuty > LIMIT_GODZINOWY:
        return OPLATA_DOBOWA
    godziny = math.ceil(minuty / 60)
    return STAWKA_ZA_GODZINE * godziny
