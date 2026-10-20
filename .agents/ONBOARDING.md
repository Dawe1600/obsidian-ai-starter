# 🚀 Procedura Onboardingu: Dynamiczny Kreator Sejfu i Asystenta

> [!IMPORTANT] Instrukcja dla Agenta
> Ten dokument jest uruchamiany automatycznie przy pierwszym kontakcie z użytkownikiem, gdy plik `.agents/SOUL.md` zawiera znacznik `[SZABLON DO SKONFIGUROWANIA]`.
> Twoim celem jest przeprowadzenie szybkiego, inteligentnego wywiadu w 3 krokach i fizyczna konfiguracja środowiska.

---

### Krok 1: Diagnoza Roli i Potrzeb (Twoja pierwsza odpowiedź)
Przywitaj użytkownika krótko i naturalnie. Wyjaśnij, że w 3 szybkich krokach dopasujesz charakter asystenta, strukturę sejfu Obsidian oraz reguły pracy pod jego potrzeby, a następnie zadaj **BLOK 1**:
1. *Kim jesteś i czym zajmujesz się na co dzień? (Twoja rola zawodowa / branża / studia)*
2. *Do czego przede wszystkim ma służyć ten sejf? (zarządzanie zadaniami, baza wiedzy, prowadzenie projektów, studia, praca czy organizacja prywatna?)*

---

### Krok 2: Rekomendacja Struktury Sejfu + Styl Asystenta
Po uzyskaniu odpowiedzi na Blok 1:
1. **Zaproponuj dopasowaną strukturę folderów w sejfie:**
   * Dla **IT / Inżynierii / AI:** `Projekty/`, `Baza Wiedzy/`, `Zadania/`, `Architektura/`, `Daily Notes/`
   * Dla **Studentów / Uczelni:** `Studia/`, `Przedmioty/`, `Egzaminy/`, `Zadania/`, `Baza Wiedzy/`, `Daily Notes/`
   * Dla **Biznesu, Menedżerów i Freelancerów:** `Klienci/`, `Spotkania/`, `Projekty/`, `Finanse/`, `Zadania/`, `Daily Notes/`
   * Dla **Twórców Treści i Marketingu:** `Scenariusze/`, `Pomysły/`, `Kampanie/`, `Research/`, `Zadania/`, `Daily Notes/`
   * Dla **Struktury Zbalansowanej (Praca + Studia + Życie):** `Praca/`, `Studia/`, `Projekty/`, `Baza Wiedzy/`, `Zadania/`, `Osobiste/`, `Daily Notes/`
   * Dla **Metodologii PARA:** `01_Projects/`, `02_Areas/`, `03_Resources/`, `04_Archive/`, `Daily Notes/`
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

### Krok 4: Fizyczna Budowa Sejfu i Samomodyfikacja (Wykonywane w tle)
Po uzyskaniu odpowiedzi na Krok 3 wykonaj natychmiast następujące czynności:
1. **Zbuduj foldery w `sejf/`:**
   Utwórz zaakceptowane foldery (np. `sejf/Praca/`, `sejf/Studia/`, `sejf/Projekty/` itp.) oraz zachowaj `sejf/Daily Notes/` i `sejf/Zadania/`.
2. **Przebuduj `sejf/Pulpit.md`:**
   Nadpisz ten plik nowym, czystym dashboardem łączącym się z głównymi hubami kategorii (zgodnie z regułą higieny grafu).
3. **Nadpisz `.agents/SOUL.md`:**
   Usuń znacznik `[SZABLON DO SKONFIGUROWANIA]` i uzupełnij 4 filary (Tożsamość, Ton głosu, Relacja, Zasady behawioralne i granice). Wpisz zasadę braku m-dashów, domyślnego zapisu w sejfie i zakazu zmyślania faktów.
4. **Zaktualizuj `.agents/MEMORY.md`:**
   Uzupełnij profil użytkownika, cele, preferencje i wpisz wpis startowy w Historii Zmian Pamięci.
5. **Dostosuj `.agents/AGENTS.md`:**
   Zaktualizuj sekcję „Mapa Katalogów” do nowej struktury folderów oraz usuń sekcję „Pierwsze Uruchomienie (Kreator Sejfu)”.
6. **Usuń ten plik (`.agents/ONBOARDING.md`):**
   Kreator spełnił swoje zadanie: usuń fizycznie plik `ONBOARDING.md`, aby nie zaśmiecał katalogu `.agents/`.
7. **Przywitaj użytkownika w nowej roli:**
   Potwierdź, że konfiguracja zakończyła się sukcesem i sejf jest w 100% gotowy do pracy!
