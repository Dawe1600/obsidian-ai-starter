---
name: obsidian-manager
description: Standardy tworzenia, linkowania i zarządzania notatkami w sejfie Obsidian. Używaj przy każdej operacji na plikach w folderze sejf/.
---

# 📚 Skill: Obsidian Manager

Ta umiejętność definiuje standardy formatowania, strukturyzowania oraz linkowania wiedzy w sejfie Obsidian (`sejf/`).

---

## 1. Architektura Wikilinków (`[[...]]`)
Każda nowo tworzona notatka musi być powiązana z istniejącą siatką wiedzy:
* Używaj formatu `[[Folder/Nazwa Notatki|Wyświetlany Tekst]]` lub bezpośredniego `[[Nazwa Notatki]]`.
* Zawsze linkuj do projektów z folderu `sejf/Projekty/` i tematów z `sejf/Baza Wiedzy/`.
* Gdy wspominasz o zadaniach, twórz link do `[[Zadania/Zadania|Zadania]]`.

---

## 2. Higiena Grafu i Reguła Pulpitu
Wizualizacja grafu w Obsidianie to potężne narzędzie pod warunkiem zachowania hierarchii:
* **Pulpit jako jedyny punkt wejścia**: `[[Pulpit]]` linkuje wyłącznie do głównych hubów kategorii (przeglądów folderów).
* **Zakaz linkowania z powrotem do Pulpitu**: Żadne notatki szczegółowe, projekty, procedury ani notatki dzienne (`Daily Notes`) nie mogą linkować do `[[Pulpit]]`. Pozwala to uniknąć efektu zaśmieconej gwiazdy w widoku grafu.
* Notatki łączą się horyzontalnie między sobą (np. projekt łączy się z bazą wiedzy i zadaniem).

---

## 3. Zapis Ustaleń i Zakaz Zmyślania
* **Domyślny zapis w sejfie**: Wszystkie ustalenia, plany projektowe, architektura i decyzje wypracowane w rozmowie powinny domyślnie trafiać do odpowiednich notatek w `sejf/`.
* **Zakaz halucynacji**: Bezwzględny zakaz wymyślania nieomówionych faktów, zadań czy dat.
* **Pytaj przy wątpliwościach**: Jeśli nie jest jasne, do której kategorii przypisać notatkę lub intencja użytkownika jest niejednoznaczna, zapytaj wprost.

---

## 4. Standardy Wizualne i Callouts
Stosuj bloki wyróżnień (Callouts) zgodne z Obsidianem:
* `> [!NOTE]`: Ważny kontekst, tło sprawy.
* `> [!TIP]`: Porada, trik, szybsze rozwiązanie.
* `> [!IMPORTANT]`: Kluczowe ustalenie, krytyczny punkt.
* `> [!WARNING]`: Uwaga na błędy, ryzyko, niesprawdzone procedury.

---

## 5. Czysta Typografia
* **Brak m-dashów**: Unikaj znaków pauzy ('—') oraz półpauzy ('–'). Stosuj wyłącznie standardowy łącznik '-' lub dwukropek ':'.
* **Tagi**: Dodawaj spójne tagi na końcu notatek (np. `#projekt`, `#zadanie`, `#procedura`, `#wiedza`).

---

## 6. Struktura Nowych Notatek w Bazie Wiedzy
Gdy tworzysz nową procedurę lub opis problemu w `sejf/Baza Wiedzy/`, stosuj schemat:
```markdown
# 🛠️ [Nazwa Zagadnienia / Procedury]

> [!NOTE] Opis
> Krótkie 1-2 zdaniowe podsumowanie czego dotyczy ta notatka.

---

## 📋 Wymagania / Kontekst
* 

## ⚙️ Krok po kroku
1. 

## 🔗 Powiązania
* Powiązany projekt: [[Projekty/...]]
* Zadania: [[Zadania/Zadania|Zadania]]

---
#wiedza #procedura
```

---

## 7. Szacunek dla Struktury
* Nigdy nie twórz tymczasowych notatek roboczych bezpośrednio w głównym katalogu `sejf/`.
* Jeśli notatka nie pasuje do istniejących folderów, spytaj użytkownika lub zapisz ją w `sejf/Baza Wiedzy/`.
