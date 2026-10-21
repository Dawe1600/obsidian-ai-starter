---
name: vault-lint
description: Audyt higieny sejfu Obsidian. Uruchamiaj na żądanie użytkownika lub cyklicznie, aby wykryć naruszenia reguły Pulpitu, martwe wikilinki, osierocone notatki i brakujące tagi.
---

# 🧹 Skill: Vault Lint (Audyt Higieny i Spójności Sejfu)

Ta umiejętność służy do weryfikacji zdrowia i czystości sejfu Obsidian (`sejf/`). Zapobiega degradacji bazy wiedzy, powstawaniu martwych linków oraz zaśmiecaniu widoku grafu.

---

## 🚀 Sposób Uruchomienia

### Krok 1: Wykonanie audytu
Wykonaj skrypt w terminalu:
```bash
python .agents/scripts/vault_lint.py
```

*Zasada fallbacku:* Jeśli Python nie jest zainstalowany w systemie, przeprowadź audyt ręcznie na plikach Markdown w katalogu `sejf/`, sprawdzając poniższe reguły.

---

## 🔍 Weryfikowane Obszary

1. **Reguła Pulpitu (Higiena Grafu Wiedzy):**
   * Żadna notatka podrzędna (z folderów `Projekty/`, `Baza Wiedzy/`, `Zadania/`, `Daily Notes/`) nie może linkować wstecznie do `[[Pulpit]]`.
   * Tylko `Pulpit.md` linkuje do głównych hubów. Naruszenia są flagowane jako błędy niszczące czytelność grafu powiązań.

2. **Martwe Wikilinki:**
   * Wykrywa odnośniki w formacie `[[Nazwa Notatki]]`, które nie wskazują na żaden istniejący plik w `sejf/`.

3. **Osierocone Notatki (Orphans):**
   * Pliki, do których nie prowadzi żaden odnośnik z innych notatek i które same nigdzie nie linkują. Każda notatka powinna być wpięta w sieć wiedzy.

4. **Brakujące Tagi:**
   * Notatki w folderach `sejf/Projekty/` i `sejf/Baza Wiedzy/` muszą posiadać co najmniej jeden tag tematyczny (np. `#projekt`, `#wiedza`).

5. **Puste Notatki:**
   * Pliki o zerowej objętości lub pozbawione treści.

---

## 🛠️ Procedura Naprawcza po Audycie

1. **Przedstawienie wyników:** Zaprezentuj użytkownikowi zwięzłe podsumowanie wykrytych uwag.
2. **Propozycja naprawy:**
   * Dla naruszeń Pulpitu: zaproponuj usunięcie linku `[[Pulpit]]` lub zastąpienie go linkiem do właściwego huba kategorii.
   * Dla martwych wikilinków: zapytaj czy utworzyć brakującą notatkę ze szablonu, czy poprawić literówkę w nazwie.
   * Dla osieroconych notatek: zaproponuj powiązanie ich z odpowiednim projektem lub bazą wiedzy.
3. **Akceptacja i wdrożenie:** Po potwierdzeniu przez użytkownika wprowadź poprawki bezpośrednio w plikach sejfu.
