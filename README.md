# 🧠 Obsidian + AI Agent Starter Pack

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Obsidian](https://img.shields.io/badge/Obsidian-v1.0+-7C3AED.svg?logo=obsidian&logoColor=white)](https://obsidian.md)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB.svg?logo=python&logoColor=white)](https://python.org)
[![Privacy](https://img.shields.io/badge/Prywatno%C5%9B%C4%87-100%25_Lokalnie-orange.svg)]()

> Gotowy, modularny szablon łączący Twój lokalny sejf notatek **Obsidian** z autonomicznym **Agentem AI** (np. Antigravity, Claude Code, Cursor, Windsurf) i dowolnym wybranym modelem.

---

## 🏗️ Architektura: Separacja Logiki od Danych (Separation of Concerns)

Większość poradników uczy wrzucania plików konfiguracyjnych bezpośrednio do sejfu notatek. W tym szablonie zastosowano czystą architekturę inżynierską:

```text
WORKSPACE/
├── .agents/                      <-- 🤖 Warstwa operacyjna (Mózg Agenta)
│   ├── SOUL.md                   # Tożsamość, charakter i styl asystenta
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
4. **Osobowość skrojona na miarę:** W pliku `SOUL.md` asystent przechowuje swój charakter, ton głosu i model relacji z Tobą.

---

## 🚀 Szybki Start w 3 Krokach

### Krok 1: Pobierz szablon
Sklonuj to repozytorium na swój dysk:
```bash
git clone https://github.com/Dawe1600/obsidian-ai-starter.git
```

### Krok 2: Otwórz Workspace i Skonfiguruj Asystenta
1. Uruchom swoje narzędzie agencyjne (np. **Antigravity**, **Cursor**, **Claude Code**, **Cline**, **Windsurf** itp.).
2. Jako katalog roboczy (Workspace) otwórz **główny folder projektu** (ten zawierający zarówno `.agents/`, jak i `sejf/`).
3. Wybierz swój preferowany model (np. Claude, Gemini, GPT lub model lokalny).
4. Napisz dowolną pierwszą wiadomość (np. *„Cześć, zacznijmy!”*).
   * Agent automatycznie wykryje pierwsze uruchomienie, przeprowadzi krótki wywiad w 3 krokach i sam zbuduje strukturę sejfu oraz skonfiguruje pliki `SOUL.md`, `AGENTS.md` i `MEMORY.md`.

### Krok 3: Otwórz Sejf w Obsidianie
1. Uruchom program **Obsidian**.
2. Kliknij **Otwórz folder jako sejf** (Open folder as vault).
3. Wskaż podfolder `sejf/` i ciesz się gotowym, spersonalizowanym centrum dowodzenia!

---

## ⚙️ Wbudowane Skrypty

W folderze `.agents/scripts/` znajduje się gotowy skrypt w czystym standardowym Pythonie 3 (zero zewnętrznych instalacji `pip`):
* `daily_note.py` — automatycznie tworzy nową notatkę dzienną w `sejf/Daily Notes/YYYY-MM-DD.md` i zaciąga aktywne zadania z pliku `sejf/Zadania/Zadania.md`.

Uruchomienie w terminalu:
```bash
python .agents/scripts/daily_note.py
```

> [!TIP] Brak Pythona na komputerze? Żaden problem!
> Skrypt Pythona to tylko opcjonalne ułatwienie. Twój asystent AI potrafi wykonać dokładnie to samo bezpośrednio w oknie czatu — wystarczy napisać: *„Wygeneruj moją notatkę na dziś”*, a agent utworzy plik sam, bez potrzeby instalowania czegokolwiek.

---

## ❓ Najczęściej Zadawane Pytania (FAQ)

### Czy to działa na Windowsie, macOS i Linuksie?
Tak. Zarówno pliki Markdown w Obsidianie, jak i skrypt w standardowym Pythonie 3 działają w 100% identycznie na każdym systemie operacyjnym.

### Czy muszę płacić za modele AI?
Nie. Możesz używać darmowych kluczy API (np. darmowy poziom Google AI Studio z modelem Gemini Flash) lub uruchomić całkowicie darmowy lokalny model na własnym komputerze przez Ollama (np. Llama 3, Qwen, Mistral).

### Czy moje notatki i dane są prywatne?
Tak. Cały sejf notatek oraz logika agenta żyją w 100% lokalnie na Twoim dysku twardym. Dane trafiają do modelu AI tylko wtedy, gdy sam zadasz pytanie w oknie agenta. Zero automatycznej telemetrii i pełna kontrola nad Twoimi plikami.

### Co jeśli nie mam lub nie znam Pythona?
Nie musisz mieć ani znać Pythona! Twój asystent AI potrafi wykonać wszystkie operacje bezpośrednio na plikach Markdown w oknie czatu. Jeśli jednak chcesz korzystać ze skryptu w tle, możesz zainstalować Pythona w 10 sekund jedną komendą:
* **Windows (PowerShell):** `winget install Python.Python.3.12`
* **macOS:** `brew install python`
* **Linux:** `sudo apt install python3`

---

## 📄 Licencja & Społeczność
Szablon jest całkowicie darmowy (licencja MIT). Możesz go dowolnie modyfikować i dopasowywać pod swój workflow.
