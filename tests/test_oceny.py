"""Testy czarnoskrzynkowe: ocena_z_procentow (OC-1 ... OC-4)."""
import pytest

from sut import ocena_z_procentow


# EP – klasy poprawne: jedna typowa wartość z każdej klasy
@pytest.mark.parametrize("procent, ocena", [
    pytest.param(25, 2.0, id="ndst"),
    pytest.param(55, 3.0, id="dst"),
    # TODO: po jednej wartości dla ocen 3.5, 4.0, 4.5 i 5.0
])
def test_ep_klasy_poprawne(procent, ocena):
    assert ocena_z_procentow(procent) == ocena


# EP – klasy niepoprawne (wartość): jeden test = jedna klasa
@pytest.mark.parametrize("procent", [
    pytest.param(-10, id="ujemny"),
    # TODO: klasa "powyżej 100"
])
def test_ep_poza_zakresem(procent):
    with pytest.raises(ValueError):
        ocena_z_procentow(procent)


# TODO: test_ep_zly_typ – argumenty innego typu niż int (OC-4)


# TODO: test_awb_2p – wszystkie wartości AWB 2-punktowej


# TODO: test_awb_3p_dodatkowe – wartości, które dokłada
#       wersja 3-punktowa (tych, które są już w 2p, nie powtarzaj)
