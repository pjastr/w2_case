"""Walidacja hasła przy zakładaniu konta."""

MIN_DL = 8
MAX_DL = 20


def waliduj_haslo(haslo):
    """Zwraca True, gdy hasło spełnia reguły, a w innym razie False.

    Wymagania: SPECYFIKACJA.md, punkty HS-1 ... HS-4.
    """
    if not isinstance(haslo, str):
        raise TypeError("hasło musi być napisem (str)")
    if len(haslo) < MIN_DL or len(haslo) > MAX_DL:
        return False
    if not haslo.isalnum():
        return False
    ma_litere = any(znak.isalpha() for znak in haslo)
    ma_cyfre = any(znak.isdigit() for znak in haslo)
    return ma_litere and ma_cyfre
