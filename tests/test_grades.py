"""Testy czarnoskrzynkowe: grade_from_percent (OC-1 ... OC-4)."""
import pytest

from sut import grade_from_percent


# EP – klasy poprawne: jedna typowa wartość z każdej klasy
@pytest.mark.parametrize("percent, grade", [
    pytest.param(25, 2.0, id="fail"),
    pytest.param(55, 3.0, id="satisfactory"),
    # TODO: po jednej wartości dla ocen 3.5, 4.0, 4.5 i 5.0
])
def test_ep_valid_classes(percent, grade):
    assert grade_from_percent(percent) == grade


# EP – klasy niepoprawne (wartość): jeden test = jedna klasa
@pytest.mark.parametrize("percent", [
    pytest.param(-10, id="negative"),
    # TODO: klasa "powyżej 100"
])
def test_ep_out_of_range(percent):
    with pytest.raises(ValueError):
        grade_from_percent(percent)


# TODO: test_ep_wrong_type – argumenty innego typu niż int (OC-4)


# TODO: test_bva_2p – wszystkie wartości AWB 2-punktowej


# TODO: test_bva_3p_extra – wartości, które dokłada
#       wersja 3-punktowa (tych, które są już w 2p, nie powtarzaj)
