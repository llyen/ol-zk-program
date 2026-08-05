# Wspólne konwencje — program demo „Ochrona Ludności i Zarządzanie Kryzysowe"

Dokument obowiązuje wszystkie repozytoria scenariuszy w `C:\repos\OchronaLudnosci\`.

---

## 1. Kontekst merytoryczny (źródło: prezentacja „ZK i OL")

- **Podstawa prawna:** Ustawa z 26 kwietnia 2007 r. o zarządzaniu kryzysowym (Dz. U. 2007 Nr 89 poz. 590).
- **Cztery fazy ZK:** zapobieganie → przygotowanie → reagowanie → odbudowa (usuwanie skutków i odtwarzanie zasobów/IK).
- **Rozróżnienie:**
  - *Zarządzanie kryzysowe* — skierowane na administrację (uruchomienie zespołów ZK, koordynacja resortów/wojska/samorządów, decyzja o uruchomieniu rezerw, procedury KPZK).
  - *Ochrona ludności* — skierowana na człowieka (ewakuacja, schronienie, żywność, opieka medyczna, wydawanie agregatów, plany OL).
- **Poziomy reagowania:** gmina → powiat → wojewoda (gdy brak sił i środków w powiecie) → minister wiodący → **RZZK** (gdy zaangażowanych kilku ministrów lub brak sił i środków jednego ministra).
- **RZZK** — organ opiniodawczo-doradczy; skład: Premier (przewodniczący), MON i MSWiA (zastępcy), MSZ i minister-koordynator (członkowie), BBN (prawo udziału), Dyrektor RCB (sekretarz).

### 20 zagrożeń KPZK (kanoniczna lista — używać tych nazw i kodów)

| Kod | Zagrożenie | Prawdopod. | Skutki |
|---|---|---|---|
| Z01 | Epidemia | możliwe | katastrofalne |
| Z02 | Powódź | prawdopodobne | duże |
| Z03 | Zakłócenie funkcjonowania systemów i sieci teleinformatycznych | możliwe | duże |
| Z04 | Działania hybrydowe | możliwe | duże |
| Z05 | Susza/upał | prawdopodobne | średnie |
| Z06 | Epizootia | prawdopodobne | średnie |
| Z07 | Zakłócenie w systemie energetycznym | prawdopodobne | średnie |
| Z08 | Silny wiatr | prawdopodobne | średnie |
| Z09 | Zakłócenie w systemie paliwowym | możliwe | średnie |
| Z10 | Pożar wielkopowierzchniowy | możliwe | średnie |
| Z11 | Epifitoza | możliwe | średnie |
| Z12 | Zakłócenie funkcjonowania systemów i usług telekomunikacyjnych | możliwe | średnie |
| Z13 | Skażenie chemiczne na lądzie | rzadkie | małe |
| Z14 | Zakłócenie w systemie gazowym | rzadkie | średnie |
| Z15 | Katastrofa morska | rzadkie | średnie |
| Z16 | Zdarzenie o charakterze terrorystycznym | bardzo rzadkie | duże |
| Z17 | Skażenie promieniotwórcze | bardzo rzadkie | duże |
| Z18 | Zbiorowe zakłócenie porządku publicznego | prawdopodobne | małe |
| Z19 | Silny mróz/intensywne opady śniegu | możliwe | małe |
| Z20 | Dezinformacja | (nieujęte w matrycy) | — |

Skale matrycy ryzyka:
- Prawdopodobieństwo: `bardzo rzadkie < rzadkie < możliwe < prawdopodobne < bardzo prawdopodobne` (1–5)
- Skutki: `nieistotne < małe < średnie < duże < katastrofalne` (1–5)
- Kolor: zielony (1–6), żółty (7–14), czerwony (15–24), brązowy/krytyczny (25)

### 16 Standardowych Procedur Operacyjnych (SPO)

| Kod | Nazwa |
|---|---|
| SPO-1 | Organizacja posiedzenia Rządowego Zespołu Zarządzania Kryzysowego |
| SPO-2 | Uruchomienie dodatkowych środków finansowych |
| SPO-3 | Zasady informowania ludności o zagrożeniach – organizacja procesu komunikacji społecznej w sytuacji kryzysowej |
| SPO-4 | Tymczasowe przywrócenie kontroli granicznej na granicach RP |
| SPO-5 | Wprowadzenie stanu klęski żywiołowej |
| SPO-6 | Wprowadzenie stanu wyjątkowego |
| SPO-7 | Wprowadzenie stanu wojennego |
| SPO-8 | Postępowanie w sytuacji uprowadzenia terrorystycznego obywatela polskiego poza obszarem RP |
| SPO-9 | Działania w przypadku masowego napływu cudzoziemców na terytorium RP |
| SPO-10 | Współpraca między administracją publiczną a właścicielami oraz posiadaczami samoistnymi i zależnymi obiektów, instalacji lub urządzeń infrastruktury krytycznej w zakresie jej ochrony |
| SPO-11 | Organizacja ewakuacji obywateli polskich spoza granic kraju |
| SPO-12 | Obieg informacji pomiędzy krajowymi organami i strukturami zarządzania kryzysowego |
| SPO-13 | Ostrzeganie i alarmowanie wojsk oraz ludności cywilnej o zagrożeniu uderzeniami z powietrza |
| SPO-14 | Przekraczanie granic RP przez wojska sojusznicze w celu pobytu lub tranzytu |
| SPO-15 | Organizacja medycznego mostu powietrznego w przypadku wystąpienia zdarzenia masowego |
| SPO-16 | Zwołanie i obsługa posiedzenia Zespołu do spraw Incydentów Krytycznych |

### Działy administracji rządowej (siatka bezpieczeństwa) — numeracja katalogowa

I Administracja publiczna · II Budownictwo/planowanie przestrzenne i mieszkalnictwo · III Budżet · IV Energia · V Finanse publiczne · VI Gospodarka · VII Gospodarka morska · VIII Gospodarka wodna · IX Zdrowie · X Informatyzacja · XI Kultura i ochrona dziedzictwa narodowego · XII Kultura fizyczna · XIII Łączność · XIV Obrona narodowa · XV Oświata i wychowanie · XVI Praca · XVII Rolnictwo · XVIII Sprawiedliwość · XIX Sprawy wewnętrzne · XX Sprawy zagraniczne · XXI Środowisko · XXII Transport · XXIII Zabezpieczenie społeczne · XXIV Klimat · XXV Aktywa państwowe

Fazy w siatce: **R** – reagowanie, **O** – odbudowa. Komórka zawiera numery modułów zadaniowych (1–7).

---

## 2. Scenariusz osiowy (wspólny dla wszystkich repo)

**„POWÓDŹ WRZESIEŃ" — zdarzenie referencyjne**

- Dorzecze Odry i Nysy Kłodzkiej; ogniska: Kotlina Kłodzka (Kłodzko, Bystrzyca Kłodzka, Lądek-Zdrój, Stronie Śląskie), Nysa, Opole, Wrocław.
- Województwa najbardziej dotknięte: **dolnośląskie (02)**, **opolskie (16)**, dalej śląskie (24), lubuskie (08), zachodniopomorskie (32).
- Perspektywa: **krajowa (RCB / RZZK)** — dashboard pokazuje wszystkie 16 województw, drill-down do powiatu/gminy.
- Oś czasu demo: **D-3 … D+10** (D0 = przekroczenie stanów alarmowych i zwołanie RZZK).
- Zagrożenia współwystępujące (do fuzji): Z02 Powódź (główne), Z07 Energetyka, Z12 Telekomunikacja, Z20 Dezinformacja.

Repozytorium `ol-blackout-wrazliwi` używa scenariusza pobocznego **„MRÓZ STYCZEŃ"** (Z19 + Z07) — również ujęcie krajowe.

---

## 3. Konwencje danych syntetycznych

- Generator: `generate_datasets.py`, **`random.seed(42)` i `numpy.random.default_rng(42)`** — pełna powtarzalność.
- Format wsadowy: `datasets/*.csv` (wymiary) + `datasets/*.jsonl` (zdarzenia/telemetria).
- Kodowanie: **UTF-8**, separator CSV `,`, dziesiętny `.`, daty ISO-8601 z offsetem `+02:00`.
- Geografia: syntetyczne kody w formacie TERYT (woj. 2 znaki, powiat 4, gmina 7). Nazwy województw i głównych miast prawdziwe; nazwy gmin/obiektów mogą być syntetyczne, ale realistyczne.
- **Każdy plik danych musi mieć nagłówek/disclaimer w README: dane w 100% syntetyczne, nie stanowią danych operacyjnych żadnej instytucji.**
- Symulator real-time: `simulate_realtime.py` — wysyłka do Eventstream (custom endpoint / Event Hub) z parametrami `--speed`, `--from`, `--to`, `--dry-run` (tryb offline zapisuje do pliku). Musi działać bez poświadczeń w `--dry-run`.

## 4. Wymagana zawartość każdego repozytorium

```
<repo>/
├── README.md                  # cel, architektura, jak uruchomić, disclaimer
├── DEMO_SCRIPT.md             # narracja demo: role, oś czasu, co mówić, co klikać, "wow moments"
├── SETUP_FABRIC.md            # krok po kroku: workspace, Lakehouse/Eventhouse, Eventstream, Dashboard, Data Agent, Fabric App
├── ARCHITECTURE.md + architecture.mmd   # diagram Mermaid
├── DATA_MODEL.md              # słownik danych (tabele, kolumny, typy, ziarno)
├── generate_datasets.py       # generator danych (seed=42)
├── simulate_realtime.py       # symulator strumienia (jeśli scenariusz RTI)
├── requirements.txt
├── datasets/                  # wygenerowane dane
├── kql/                       # skrypty KQL: schematy, update policies, zapytania dashboardu
├── notebooks/                 # notatniki Fabric (.py z komórkami # CELL lub .ipynb)
├── semantic-model/            # opis modelu semantycznego + miary DAX
├── fabric-app/                # specyfikacja aplikacji (Rayfin/Fabric Apps): ekrany, pola, akcje, prompt do generatora
├── activator/                 # definicje reguł alertowych
└── LICENSE                    # MIT
```

Język dokumentacji: **polski**. Nazwy techniczne (tabele, kolumny) po angielsku, bez polskich znaków.

## 5. Fabric — mapowanie funkcji

| Funkcja | Zastosowanie |
|---|---|
| Eventstream | wejście telemetrii (hydro, energetyka, zgłoszenia 112, statusy zasobów) |
| Eventhouse / KQL DB | dane real-time, korelacje, anomalie |
| Lakehouse (Delta) | wymiary, rejestry, dane referencyjne, wyniki analiz |
| Data Warehouse | warstwa raportowa T-SQL tam, gdzie potrzebna |
| Notebooki (PySpark/Python) | scoring ryzyka, optymalizacja, symulacje |
| Data Pipelines | orkiestracja wsadów i odświeżeń |
| Real-Time Dashboard | operacyjny obraz sytuacji (KQL) |
| Power BI + model semantyczny | warstwa decyzyjna, drill-down, mobile |
| Data Activator (Reflex) | reguły progowe → alert do Teams / e-mail / akcja |
| Data Agent / AI Skill | pytania w języku naturalnym o sytuację i procedury |
| AI Functions | klasyfikacja zgłoszeń, streszczenia, wykrywanie narracji |
| **Fabric Apps / Rayfin** | aplikacje operatorskie: karta ewakuacji, wniosek o zasób, checklisty SPO |
| OneLake shortcuts | współdzielenie danych między repo/scenariuszami |
| Purview / etykiety wrażliwości | ochrona danych osobowych i informacji niejawnych (opis) |

## 6. Zasady bezpieczeństwa demo

- Zero prawdziwych danych osobowych; PESEL/adresy generowane syntetycznie i oznaczone jako fikcyjne.
- Brak poświadczeń w repo — konfiguracja przez `.env` (w `.gitignore`) i `config.example.json`.
- Każdy README zaczyna się disclaimerem o charakterze demonstracyjnym.

## 7. Wygląd aplikacji Fabric — obowiązująca paleta

**Wszystkie aplikacje są jasne, w barwach rządowych (gov.pl / MSWiA).** Nowa aplikacja nie
może powstać w ciemnym motywie. Paleta pochodzi wprost z arkusza stylów gov.pl
(`https://www.gov.pl/css/govpl_template.css`), nie z oszacowania.

Tokeny do wklejenia w `src/main.css` (osobny blok `@theme`, **nie** `@theme inline` —
ten drugi służy do odwołań między zmiennymi):

```css
@theme {
  --color-gov: #0052a5;
  --color-gov-dark: #00417f;
  --color-gov-light: #006cd7;
  --color-gov-50: #e8eef7;
  --color-gov-ink: #1b1b1b;
  --color-gov-red: #d5233f;
}
```

Wzorcem konwencji jest `ol-siatka-bezpieczenstwa/fabric-app/pulpit-koordynacji/src/components/ui.tsx`.
Stamtąd brać wygląd kart, plakietek i przycisków:

| Element | Klasy |
|---|---|
| strona | `bg-slate-100 text-slate-900` |
| karta | `rounded-lg border border-slate-200 bg-white shadow-sm` |
| tytuł / opis | `text-slate-900` / `text-slate-500` |
| plakietka | `bg-*-100 text-*-800 ring-*-600/30` lub `bg-*-50 text-*-700 ring-*-600/30` |
| przycisk główny | `bg-gov hover:bg-gov-dark text-white` |
| nagłówek | biały, nad nim pasek `<div className="h-1 w-full bg-gov" />` |

Bez godła RP (kwestia praw do znaku).

### Czerwień jest sygnałem, nie barwą marki

`#d5233f` koduje powagę sytuacji. Użyta w nagłówku albo na przycisku „Zapisz" traci siłę
sygnału dokładnie wtedy, kiedy jest potrzebna. Nagłówki i przyciski są błękitne.

### Skale porządkowe

Jednolita skala powagi we wszystkich aplikacjach — cztery rozróżnialne stopnie:

```text
#15803d  →  #a16207  →  #c2410c  →  #d5233f
zielony     bursztyn    pomarańcz   czerwień gov
```

**Każdy poziom musi mieć własną barwę i musi to sprawdzać test.** Odwzorowanie barw przy
przechodzeniu na jasną paletę jest wiele-do-jednego, więc potrafi skleić dwa sąsiednie
stopnie w jeden kolor. Kompilacja i testy funkcjonalne tego nie wykryją — mapa po prostu
przestaje rozróżniać stan spokojny od podwyższonego.

### Narzędzia

| Skrypt | Zastosowanie |
|---|---|
| `_program/tools/retheme_gov.py` | jednorazowe przemalowanie aplikacji z ciemnego motywu; bez `--apply` robi próbę na sucho i wypisuje klasy bez odwzorowania |
| `_program/tools/audit_contrast.py` | audyt kontrastu WCAG par `bg-*`/`text-*`; ma kończyć się wynikiem **0** |

Kompilator nie wykryje jasnego napisu na jasnym tle. `audit_contrast.py` uruchamiać po
każdej większej zmianie wyglądu.

Przezroczystość nie przenosi się między motywami: `bg-amber-500/10` na ciemnym tle to
czytelny odcień, na jasnym praktycznie znika. Przy powierzchniach porzucać przezroczystość,
przy obwódkach zachowywać (`ring-*-600/30`). Wyjątek — **przykrycie okna modalnego** musi
pozostać przezroczyste (`bg-slate-900/40`), inaczej gubi kontekst pod spodem.
