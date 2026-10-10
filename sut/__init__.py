"""Moduły testowane na ćwiczeniach 2 (testy czarnoskrzynkowe).

Testy projektujemy WYŁĄCZNIE na podstawie pliku SPECYFIKACJA.md.
Nie czytaj kodu w tym katalogu przed zakończeniem ćwiczenia.
"""
from .hasla import waliduj_haslo
from .oceny import ocena_z_procentow
from .parking import oplata_parkingowa

__all__ = ["ocena_z_procentow", "oplata_parkingowa",
           "waliduj_haslo"]
