"""Pierwsze testy – sprawdzenie, czy pytest działa w projekcie."""


def dodaj(a, b):
    return a + b


def test_dodawanie_liczb_calkowitych():
    assert dodaj(2, 3) == 5


def test_dodawanie_ulamkow():
    # Ten test celowo NIE przechodzi – przeczytaj raport pytest!
    assert dodaj(0.1, 0.2) == 0.3
