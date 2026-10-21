#!/usr/bin/env python3
"""
vault_lint.py - Linter higieny i spójności sejfu Obsidian.
Weryfikuje regułę Pulpitu, martwe wikilinki, osierocone notatki i brakujące tagi.
Zero zewnętrznych zależności: używa wyłącznie biblioteki standardowej Pythona 3.
"""

from pathlib import Path
import re
import sys

# Zapewnienie poprawnego kodowania UTF-8 na konsoli Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def znajdz_sejf_dir() -> Path:
    """Wykrywa katalog sejfu względem skryptu lub bieżącego katalogu."""
    skrypt_dir = Path(__file__).resolve().parent
    root_dir = skrypt_dir.parents[1]
    sejf_dir = root_dir / "sejf"
    if not sejf_dir.exists():
        sejf_dir = Path.cwd() / "sejf"
    return sejf_dir

def usun_bloki_kodu(tekst: str) -> str:
    """Usuwa bloki kodu (```...```) i kod wplatany (`...`), by nie analizować fałszywych linków."""
    tekst_bez_blokow = re.sub(r"```[\s\S]*?```", "", tekst)
    tekst_czysty = re.sub(r"`[^`\n]+`", "", tekst_bez_blokow)
    return tekst_czysty

def wyciagnij_wikilinki(tekst: str) -> list:
    """Zwraca listę celów wikilinków (ścieżek/nazw bez aliasów i kotwic)."""
    czysty = usun_bloki_kodu(tekst)
    znalezione = re.findall(r"\[\[([^\]\|#\n]+)(?:#[^\]\|\n]+)?(?:\|[^\]\n]+)?\]\]", czysty)
    return [z.strip() for z in znalezione if z.strip()]

def ma_tagi(tekst: str) -> bool:
    """Sprawdza czy notatka zawiera przynajmniej jeden tag Obsidianowy (#tag)."""
    czysty = usun_bloki_kodu(tekst)
    for linia in czysty.splitlines():
        # Pomijamy nagłówki markdown (# Tytuł, ## Podtytuł)
        if re.match(r"^\s*#{1,6}\s+", linia):
            continue
        # Szukamy tagów #nazwa (litery, cyfry, myślniki, podkreślniki, slashe)
        if re.search(r"(?:^|\s)#[a-zA-Z0-9_\-\/]+(?:\s|$)", linia):
            return True
    return False

def cel_istnieje(cel: str, mapa_plikow: dict, mapa_nazw: dict) -> bool:
    """Sprawdza czy wikilink prowadzi do istniejącej notatki."""
    znormalizowany = cel.replace("\\", "/").strip().lower()
    if znormalizowany.endswith(".md"):
        znormalizowany = znormalizowany[:-3]

    # Sprawdzenie po pełnej ścieżce względnej
    if znormalizowany in mapa_plikow:
        return True

    # Sprawdzenie po samej nazwie pliku (Obsidian domyślnie pozwala na linkowanie samą nazwą)
    sama_nazwa = Path(znormalizowany).name
    if sama_nazwa in mapa_nazw:
        return True

    return False

def uruchom_audyt(sejf_dir: Path) -> int:
    if not sejf_dir.exists():
        print(f"❌ Błąd: Katalog sejfu nie istnieje: {sejf_dir}")
        return 1

    wszystkie_pliki = [p for p in sejf_dir.rglob("*.md") if p.is_file()]
    if not wszystkie_pliki:
        print(f"ℹ️  Brak plików Markdown w sejfie: {sejf_dir}")
        return 0

    # Budujemy mapy plików do szybkiego wyszukiwania
    # mapa_plikow: np. "zadania/zadania" -> Path
    # mapa_nazw: np. "zadania" -> list[Path]
    mapa_plikow = {}
    mapa_nazw = {}

    for plik in wszystkie_pliki:
        rel = plik.relative_to(sejf_dir).as_posix().lower()
        if rel.endswith(".md"):
            rel_bez_ext = rel[:-3]
        else:
            rel_bez_ext = rel
        mapa_plikow[rel_bez_ext] = plik

        stem = plik.stem.lower()
        if stem not in mapa_nazw:
            mapa_nazw[stem] = []
        mapa_nazw[stem].append(plik)

    bledy_pulpitu = []
    martwe_linki = []
    brakujace_tagi = []
    puste_pliki = []
    linki_wychodzace = {p: set() for p in wszystkie_pliki}
    linki_przychodzace = {p: set() for p in wszystkie_pliki}

    for plik in wszystkie_pliki:
        rel_path = plik.relative_to(sejf_dir).as_posix()
        try:
            tresc = plik.read_text(encoding="utf-8")
        except Exception as e:
            print(f"⚠️  Nie udało się odczytać {rel_path}: {e}")
            continue

        # 1. Puste pliki
        if len(tresc.strip()) == 0:
            puste_pliki.append(rel_path)
            continue

        wikilinki = wyciagnij_wikilinki(tresc)

        # 2. Naruszenie reguły Pulpitu (linki zwrotne z notatek podrzędnych do Pulpitu)
        if plik.name.lower() != "pulpit.md":
            for link in wikilinki:
                cel_norm = link.replace("\\", "/").strip().lower()
                if cel_norm in ("pulpit", "pulpit.md", "sejf/pulpit", "sejf/pulpit.md"):
                    bledy_pulpitu.append((rel_path, link))

        # 3. Weryfikacja poprawności wikilinków
        for link in wikilinki:
            if not cel_istnieje(link, mapa_plikow, mapa_nazw):
                martwe_linki.append((rel_path, link))
            else:
                # Zapisujemy relacje dla analizy osierocenia
                linki_wychodzace[plik].add(link.lower())
                cel_norm = link.replace("\\", "/").strip().lower()
                if cel_norm.endswith(".md"):
                    cel_norm = cel_norm[:-3]
                
                # Oznaczamy pliki docelowe
                docelowy = mapa_plikow.get(cel_norm)
                if not docelowy:
                    pasujace = mapa_nazw.get(Path(cel_norm).name, [])
                    if len(pasujace) == 1:
                        docelowy = pasujace[0]
                if docelowy:
                    linki_przychodzace[docelowy].add(plik)

        # 4. Sprawdzenie tagów w folderach Baza Wiedzy i Projekty
        rodzic = plik.parent.name.lower()
        if rodzic in ("projekty", "baza wiedzy"):
            if not ma_tagi(tresc):
                brakujace_tagi.append(rel_path)

    # 5. Wykrywanie osieroconych notatek (brak linków przychodzących i wychodzących)
    osierocone = []
    for plik in wszystkie_pliki:
        if plik.name.lower() == "pulpit.md":
            continue
        # Jeśli notatka nie ma linków przychodzących i sama nigdzie nie linkuje
        if len(linki_przychodzace[plik]) == 0 and len(linki_wychodzace[plik]) == 0:
            osierocone.append(plik.relative_to(sejf_dir).as_posix())

    # Raport końcowy
    print("=" * 60)
    print(" 🔍 RAPORT AUDYTU SEJFU OBSIDIAN (Vault Lint)")
    print("=" * 60)
    print(f"📁 Przeskanowano notatek: {len(wszystkie_pliki)}")
    print(f"📂 Ścieżka sejfu: {sejf_dir}")
    print("-" * 60)

    liczba_problemow = len(bledy_pulpitu) + len(martwe_linki) + len(osierocone) + len(puste_pliki) + len(brakujace_tagi)

    if liczba_problemow == 0:
        print("✨ Gratulacje! Twój sejf jest w 100% czysty i zgodny ze standardami:")
        print("   - Zero naruszeń reguły Pulpitu (czysty graf powiązań).")
        print("   - Wszystkie wikilinki wskazują na istniejące pliki.")
        print("   - Brak osieroconych notatek i pustych plików.")
        print("   - Projekty i baza wiedzy posiadają spójne tagi.")
        print("=" * 60)
        return 0

    if bledy_pulpitu:
        print(f"\n🚨 Naruszenia reguły Pulpitu (linki zwrotne do Pulpitu: {len(bledy_pulpitu)}):")
        print("   (Notatki szczegółowe nie powinny linkować do Pulpitu, aby nie zaśmiecać grafu)")
        for plik, link in bledy_pulpitu:
            print(f"   * {plik} -> [[{link}]]")

    if martwe_linki:
        print(f"\n⚠️  Martwe wikilinki (wskazują na nieistniejące pliki: {len(martwe_linki)}):")
        for plik, link in martwe_linki:
            print(f"   * {plik} -> [[{link}]]")

    if osierocone:
        print(f"\n🏝️  Osierocone notatki (brak linków przychodzących i wychodzących: {len(osierocone)}):")
        for plik in osierocone:
            print(f"   * {plik}")

    if brakujace_tagi:
        print(f"\n🏷️  Brakujące tagi w Projektach / Bazie Wiedzy ({len(brakujace_tagi)}):")
        for plik in brakujace_tagi:
            print(f"   * {plik}")

    if puste_pliki:
        print(f"\n📄 Puste notatki ({len(puste_pliki)}):")
        for plik in puste_pliki:
            print(f"   * {plik}")

    print("\n" + "=" * 60)
    print(f"Łącznie wykryto uwag: {liczba_problemow}")
    print("=" * 60)
    return 1

if __name__ == "__main__":
    kod = uruchom_audyt(znajdz_sejf_dir())
    sys.exit(kod)
