---
name: obsidian-manager
description: Standardy tworzenia, linkowania i zarządzania notatkami w sejfie Obsidian. Używaj przy każdej operacji na plikach w folderze sejf/.
---

# 📚 Skill: Obsidian Manager

Ta umiejętność definiuje najlepsze praktyki formatowania, strukturyzowania oraz linkowania wiedzy w sejfie Obsidian (`sejf/`).

---

## 1. Architektura Wikilinków (`[[...]]`)
Każda nowo tworzona notatka musi być powiązana z istniejącą siatką wiedzy:
* Używaj formatu `[[Folder/Nazwa Notatki|Wyświetlany Tekst]]` lub bezpośredniego `[[Nazwa Notatki]]`.
* Zawsze linkuj do projektów z folderu `sejf/Projekty/` i tematów z `sejf/Baza Wiedzy/`.
* Gdy wspominasz o zadaniach, twórz link do `[[Zadania/Zadania|Zadania]]`.

---

## 2. Standardy Wizualne i Callouts
Stosuj bloki wyróżnień (Callouts) zgodne z Obsidianem:
* `> [!NOTE]` — Ważny kontekst, tło sprawy.
* `> [!TIP]` — Porada, trik, szybsze rozwiązanie.
* `> [!IMPORTANT]` — Kluczowe ustalenie, krytyczny punkt.
* `> [!WARNING]` — Uwaga na błędy, ryzyko, niesprawdzone procedury.

---

## 3. Struktura Nowych Notatek w Bazie Wiedzy
Gdy tworzysz nową procedurę lub opis problemu w `sejf/Baza Wiedzy/`, stosuj szablon:
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
* Projekt: [[Projekty/...]]
* Tagi: #wiedza #procedura
```

---

## 4. Zasada Czystości
* Nigdy nie twórz tymczasowych notatek roboczych bezpośrednio w głównym katalogu `sejf/`.
* Jeśli notatka nie pasuje do istniejących folderów, spytaj użytkownika lub zapisz ją w `sejf/Baza Wiedzy/`.
