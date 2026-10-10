"""Testy czarnoskrzynkowe: oplata_parkingowa (PK-1 ... PK-5)."""
import pytest

from sut import oplata_parkingowa


# EP – klasy poprawne (także klasy WYJŚĆ: 0 zł, 5 zł, 10 zł ...)
@pytest.mark.parametrize("minuty, oplata", [
    pytest.param(600, 20.0, id="dobowa"),
    # TODO: pozostałe klasy poprawne
])
def test_ep_klasy_poprawne(minuty, oplata):
    assert oplata_parkingowa(minuty) == oplata


# TODO: test_ep_poza_zakresem (ValueError), test_ep_zly_typ


# TODO: test_awb_2p, test_awb_3p_dodatkowe
