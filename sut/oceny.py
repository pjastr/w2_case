"""Ocena z przedmiotu na podstawie procentu zdobytych punktów."""


def ocena_z_procentow(procent):
    """Zwraca ocenę (float) dla procentu punktów 0-100.

    Wymagania: SPECYFIKACJA.md, punkty OC-1 ... OC-4.
    """
    procent = int(procent)
    if procent < 0 or procent > 100:
        raise ValueError("procent musi być z zakresu 0-100")
    if procent >= 90:
        return 5.0
    if procent > 80:
        return 4.5
    if procent > 70:
        return 4.0
    if procent > 60:
        return 3.5
    if procent > 50:
        return 3.0
    return 2.0
