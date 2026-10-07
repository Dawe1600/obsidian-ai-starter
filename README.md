# 🧠 Obsidian + AI Agent Starter Pack

> Gotowy, modularny szablon łączący Twój lokalny sejf notatek **Obsidian** z autonomicznym **Agentem AI** (np. Antigravity, Claude Code, Cursor) napędzanym modelem Gemini.

---

## 🏗️ Architektura: Separacja Logiki od Danych (Separation of Concerns)

Większość poradników uczy wrzucania plików konfiguracyjnych bezpośrednio do sejfu notatek. W tym szablonie zastosowano czystą architekturę inżynierską:

```text
WORKSPACE/
├── .agents/                      <-- 🤖 Warstwa operacyjna (Mózg Agenta)
│   ├── AGENTS.md                 # Kodeks i zasady postępowania agenta
│   ├── MEMORY.md                 # Pamięć długoterminowa asystenta
│   ├── scripts/                  # Automatyzacje i skrypty w Pythonie
│   │   └── daily_note.py         # Generator notatki dziennej i zadań
│   └── skills/                   # Specjalistyczne umiejętności agenta
│       └── obsidian-manager/     # Standardy formatowania i wikilinków
│           └── SKILL.md
│
├── sejf/                         <-- 📓 Czysty Sejf Obsidian (Twoje Dane)
│   ├── Pulpit.md                 # Główny dashboard i centrum dowodzenia
│   ├── Zadania/                  # Aktywne listy zadań i checklisty
│   ├── Projekty/                 # Notatki projektowe
│   ├── Baza Wiedzy/              # Procedury, instrukcje i wiedza
│   └── Daily Notes/              # Notatki dzienne
│
├── .gitignore
└── README.md
```

### Dlaczego taki podział?
1. **Czystość w Obsidianie:** W aplikacji Obsidian otwierasz wyłącznie podfolder `sejf/`. Twój graf powiązań i drzewo plików są wolne od technicznych skryptów, logów i reguł.
2. **Pełna sprawczość agenta:** Otwierając katalog główny (`WORKSPACE`) w środowisku agencyjnym, agent widzi zarówno Twoje notatki w `sejf/`, jak i swoje instrukcje w `.agents/`.
3. **Pamięć na Twoim dysku:** Koniec z zamykaniem wiedzy w chmurze korporacji. Twoja pamięć AI żyje w pliku `MEMORY.md`, który możesz wersjonować w Git.

---

## 🚀 Szybki Start w 3 Krokach

### Krok 1: Pobierz szablon
Sklonuj to repozytorium na swój dysk:
```bash
git clone https://github.com/Dawe1600/obsidian-ai-starter.git
```

### Krok 2: Otwórz Sejf w Obsidianie
1. Uruchom program **Obsidian**.
2. Kliknij **Otwórz folder jako sejf** (Open folder as vault).
3. Wskaż podfolder `sejf/` z pobranego repozytorium.

### Krok 3: Otwórz Workspace w Środowisku Agencyjnym
1. Uruchom **Antigravity** (lub Claude Code / Cursor).
2. Jako katalog roboczy (Workspace) otwórz **główny folder projektu** (ten zawierający zarówno `.agents/`, jak i `sejf/`).
3. Wybierz model **Gemini 2.5/3.8 Flash** lub **Pro**.
4. Wpisz pierwsze polecenie:
   ```text
   Przeczytaj moje pliki z folderu .agents/ i powiedz mi, w czym możesz mi dzisiaj pomóc?
   ```

---

## ⚙️ Wbudowane Skrypty

W folderze `.agents/scripts/` znajduje się gotowy skrypt w czystym standardowym Pythonie 3 (zero zewnętrznych instalacji `pip`):
* `daily_note.py` — automatycznie tworzy nową notatkę dzienną w `sejf/Daily Notes/YYYY-MM-DD.md` i zaciąga aktywne zadania z pliku `sejf/Zadania/Zadania.md`.

Uruchomienie:
```bash
python .agents/scripts/daily_note.py
```

---

## 📄 Licencja & Społeczność
Szablon jest całkowicie darmowy (licencja MIT). Możesz go dowolnie modyfikować i dopasowywać pod swój workflow.
