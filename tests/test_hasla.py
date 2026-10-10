"""Testy czarnoskrzynkowe: waliduj_haslo (HS-1 ... HS-4)."""
import pytest

from sut import waliduj_haslo


def haslo_o_dlugosci(n):
    """Hasło z liter i cyfr o długości n, np. 5 -> 'a1a1a'."""
    return ("a1" * n)[:n]


def test_przyklad_haslo_poprawne():
    assert waliduj_haslo("haslo123") is True


def test_przyklad_zly_typ():
    with pytest.raises(TypeError):
        waliduj_haslo(None)


# TODO: test_ep_poprawne – klasy poprawne (HS-3, HS-4)
# TODO: test_ep_niepoprawne – każda klasa niepoprawna osobno
# TODO: test_awb_dlugosc_2p, test_awb_dlugosc_3p_dodatkowe
#       (użyj funkcji haslo_o_dlugosci)
