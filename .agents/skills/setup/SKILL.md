---
name: setup
description: Konfiguracja i personalizacja sejfu Obsidian oraz profilu asystenta. Uruchamiaj ZAWSZE przy pierwszym kontakcie, gdy plik .agents/SOUL.md zawiera znacznik [SZABLON DO SKONFIGUROWANIA], lub na wyraźne żądanie użytkownika (np. /setup, 'skonfiguruj mój sejf', 'zmień strukturę sejfu').
---

# 🚀 Skill: Setup (Kreator Sejfu i Personalizacja Asystenta)

Ta umiejętność służy do konfiguracji sejfu Obsidian oraz personalizacji agenta AI.
Uruchamia się automatycznie przy pierwszym kontakcie (gdy w `.agents/SOUL.md` widnieje znacznik `[SZABLON DO SKONFIGUROWANIA]`) lub na żądanie użytkownika chcącego zrekonfigurować swój sejf.

Twoim celem jest przeprowadzenie zwięzłego wywiadu w 3 krokach i fizyczne zbudowanie środowiska.

---

## 📋 Przebieg Wywiadu Krok po Kroku

### Krok 1: Diagnoza Roli i Potrzeb
Przywitaj użytkownika naturalnie i zwięźle. Wyjaśnij, że w 3 szybkich krokach dopasujesz strukturę folderów sejfu, charakter asystenta i reguły pracy pod jego potrzeby.
Zadaj **BLOK 1**:
1. *Kim jesteś i czym zajmujesz się na co dzień? (Twoja rola zawodowa / branża / studia)*
2. *Do czego przede wszystkim ma służyć ten sejf? (zarządzanie zadaniami, baza wiedzy, prowadzenie projektów, studia, praca czy organizacja prywatna?)*

---

### Krok 2: Rekomendacja Struktury Sejfu + Styl Asystenta
Po uzyskaniu odpowiedzi na Krok 1:
1. **Zaproponuj dopasowaną strukturę folderów w sejfie:**
   * **Dla IT / Inżynierii / AI:** `Projekty/`, `Baza Wiedzy/`, `Zadania/`, `Architektura/`, `Daily Notes/`
   * **Dla Studentów / Uczelni:** `Studia/`, `Przedmioty/`, `Egzaminy/`, `Zadania/`, `Baza Wiedzy/`, `Daily Notes/`
   * **Dla Biznesu, Menedżerów i Freelancerów:** `Klienci/`, `Spotkania/`, `Projekty/`, `Finanse/`, `Zadania/`, `Daily Notes/`
   * **Dla Twórców Treści i Marketingu:** `Scenariusze/`, `Pomysły/`, `Kampanie/`, `Research/`, `Zadania/`, `Daily Notes/`
   * **Dla Struktury Zbalansowanej (Praca + Studia + Życie):** `Praca/`, `Studia/`, `Projekty/`, `Baza Wiedzy/`, `Zadania/`, `Osobiste/`, `Daily Notes/`
   * **Dla Metodologii PARA:** `01_Projects/`, `02_Areas/`, `03_Resources/`, `04_Archive/`, `Daily Notes/`
   * Zapytaj: *„Czy taki podział Ci odpowiada, czy wolisz dodać lub zmienić foldery?”*

2. W tej samej wiadomości zadaj **BLOK 2 (Charakter i styl):**
   * *Jaki charakter ma mieć Twój asystent? (np. pragmatyczny partner inżynierski, zwięzły wykonawca, analityczny doradca?)*
   * *Jaki ton wypowiedzi preferujesz? (luźny i bezpośredni, czysto techniczny, czy formalny?)*

---

### Krok 3: Narzędzia i Standardy Pracy
Po odpowiedzi na Krok 2, zadaj **BLOK 3**:
1. *Z jakich kluczowych narzędzi lub technologii korzystasz na co dzień (np. Docker, Git, Python, M365, Notion, pakiet biurowy)?*
2. *Jaki styl odpowiedzi preferujesz? (krótkie checklisty i natychmiastowy konkret, czy bardziej szczegółowe omówienia?)*

---

## 🛠️ Fizyczna Budowa i Konfiguracja (Krok 4: W tle)

Gdy użytkownik odpowie na pytania z Kroku 3, natychmiast wykonaj operacje na plikach:

1. **Zbuduj foldery w `sejf/`:**
   Utwórz zaakceptowane foldery (np. `sejf/Praca/`, `sejf/Studia/`, `sejf/Projekty/` itp.) oraz zachowaj `sejf/Daily Notes/` i `sejf/Zadania/`.

2. **Przebuduj `sejf/Pulpit.md`:**
   Nadpisz ten plik nowym, czystym dashboardem łączącym się z głównymi hubami kategorii (zgodnie z regułą higieny grafu: Pulpit linkuje do hubów, notatki nie linkują wstecz do Pulpitu).

3. **Nadpisz `.agents/SOUL.md`:**
   Usuń znacznik `[SZABLON DO SKONFIGUROWANIA]` i uzupełnij 4 filary:
   * Tożsamość i Archetyp
   * Ton głosu i Styl komunikacji (w tym reguła braku znaków m-dash i en-dash)
   * Relacja z użytkownikiem
   * Zasady behawioralne i granice (domyślny zapis w sejfie, zakaz zmyślania faktów)

4. **Zaktualizuj `.agents/MEMORY.md`:**
   Uzupełnij profil użytkownika, aktywne obszary, narzędzia, preferencje oraz dodaj wpis startowy w sekcji *Historia Zmian Pamięci*.

5. **Wyczyść pliki demonstracyjne:**
   Jeśli w katalogu głównym istnieje folder `assets/`, usuń go (zawierał wyłącznie grafiki demonstracyjne do podglądu repozytorium na GitHubie, zbędne w prywatnym sejfie).

6. **Potwierdzenie dla użytkownika:**
   Przywitaj użytkownika w nowej roli i potwierdź, że sejf jest w 100% gotowy do codziennej pracy!
