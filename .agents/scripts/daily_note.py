#!/usr/bin/env python3
"""
daily_note.py — Generator notatki dziennej z synchronizacją zadań.
Używa wyłącznie wbudowanej biblioteki standardowej Pythona 3 (zero zewnętrznych zależności).
"""

from datetime import datetime
from pathlib import Path
import re
import sys

# Zapewnienie poprawnego kodowania UTF-8 na konsoli Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Dni tygodnia w języku polskim
DNI_TYGODNIA = [
    "Poniedziałek", "Wtorek", "Środa", "Czwartek",
    "Piątek", "Sobota", "Niedziela"
]

MIESIACE = [
    "stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca",
    "lipca", "sierpnia", "września", "października", "listopada", "grudnia"
]

def znajdz_sciezki():
    """Wykrywa ścieżki do folderu sejfu względem położenia skryptu."""
    skrypt_dir = Path(__file__).resolve().parent
    # Szukamy katalogu głównego (jeden poziom wyżej niż .agents)
    root_dir = skrypt_dir.parents[1]
    sejf_dir = root_dir / "sejf"
    
    if not sejf_dir.exists():
        # Fallback jeśli uruchomiono z innego miejsca
        sejf_dir = Path.cwd() / "sejf"
        
    daily_dir = sejf_dir / "Daily Notes"
    zadania_file = sejf_dir / "Zadania" / "Zadania.md"
    
    return sejf_dir, daily_dir, zadania_file

def pobierz_aktywne_zadania(zadania_file: Path) -> list:
    """Odczytuje niezrobione zadania (- [ ]) z pliku Zadania.md."""
    if not zadania_file.exists():
        return []
    
    aktywne = []
    tresc = zadania_file.read_text(encoding="utf-8")
    for linia in tresc.splitlines():
        # Szukamy checkboxów niezrobionych
        if re.match(r"^\s*-\s*\[\s*\]\s+", linia):
            zadanie = linia.strip()
            aktywne.append(zadanie)
    return aktywne

def generuj_notatke():
    sejf_dir, daily_dir, zadania_file = znajdz_sciezki()
    
    if not daily_dir.exists():
        daily_dir.mkdir(parents=True, exist_ok=True)
        
    teraz = datetime.now()
    data_format = teraz.strftime("%d.%m.%Y")
    dzien_tygodnia = DNI_TYGODNIA[teraz.weekday()]
    ladna_data = f"{teraz.day} {MIESIACE[teraz.month - 1]} {teraz.year} ({dzien_tygodnia})"
    
    docelowy_plik = daily_dir / f"{data_format}.md"
    
    if docelowy_plik.exists():
        print(f"ℹ️  Notatka dzienna na dzień {data_format} już istnieje:")
        print(f"   -> {docelowy_plik}")
        return
    
    zadania = pobierz_aktywne_zadania(zadania_file)
    zadania_md = "\n".join(zadania) if zadania else "- [ ] Zdefiniuj pierwsze zadanie na dziś"
    
    szablon = f"""# 📅 {ladna_data}

> [!NOTE] Podsumowanie Dnia
> Notatka dzienna wygenerowana automatycznie. Link do centralnego [[Pulpit|Pulpitu]].

---

## 🎯 Aktywne Zadania (zsynchronizowane z [[Zadania/Zadania|Zadania]])
{zadania_md}

---

## 📝 Notatki i Przebieg Dnia
* 

---

## 💡 Nowe Ustalenia & Pomysły
* 

---
#daily #{teraz.strftime("%m.%Y")}
"""

    docelowy_plik.write_text(szablon, encoding="utf-8")
    print(f"✅ Sukces: Wygenerowano nową notatkę dzienną:")
    print(f"   Plik: {docelowy_plik.name}")
    print(f"   Ścieżka: {docelowy_plik}")
    print(f"   Zsynchronizowano {len(zadania)} aktywnych zadań.")

if __name__ == "__main__":
    generuj_notatke()
