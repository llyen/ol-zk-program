# 🛡️ Ochrona Ludności i Zarządzanie Kryzysowe — program demo na Microsoft Fabric

> ⚠️ **Disclaimer** — wszystkie materiały mają charakter **demonstracyjny i edukacyjny**.
> Dane są w 100% generowane syntetycznie i nie stanowią danych operacyjnych ani
> rzeczywistych informacji jakiejkolwiek instytucji publicznej. Nazwy instytucji
> użyto wyłącznie dla realizmu narracji.

Program pokazuje, jak **Microsoft Fabric** i usługi danych wspierają zarządzanie
kryzysowe i ochronę ludności w Polsce — z perspektywy **krajowej (RCB / RZZK)**,
na poziomie zrozumiałym dla decydenta biznesowego, nie inżyniera.

Podstawa merytoryczna: Ustawa z 26 kwietnia 2007 r. o zarządzaniu kryzysowym,
Krajowy Plan Zarządzania Kryzysowego (20 zagrożeń, matryca ryzyka, siatka
bezpieczeństwa), 16 Standardowych Procedur Operacyjnych.

---

## 📦 Repozytoria scenariuszy

| Katalog | Scenariusz | Główne pytanie decydenta | Kluczowe funkcje Fabric |
|---|---|---|---|
| [`ol-cop24`](../ol-cop24/) | **COP-24 — Wspólny Obraz Sytuacji** | *Co się dzieje w kraju w tej chwili i czy muszę zwołać RZZK?* | Eventstream, Eventhouse/KQL, Real-Time Dashboard, Activator, Data Agent, Fabric App |
| [`ol-siatka-bezpieczenstwa`](../ol-siatka-bezpieczenstwa/) | **Siatka Bezpieczeństwa jako aplikacja** | *Kto za co odpowiada i czy jest gotowy?* | Lakehouse, graf odpowiedzialności, Power BI, Data Agent, **Fabric App** |
| [`ol-zasoby-logistyka`](../ol-zasoby-logistyka/) | **Zasoby i rezerwy — logistyka kryzysowa** | *Czym dysponujemy, kiedy dotrze i czy wystarczy?* | Lakehouse, optymalizacja przydziału, Eventstream (transporty), **Fabric App**, Activator |
| [`ol-blackout-wrazliwi`](../ol-blackout-wrazliwi/) | **Blackout / zima — ludność wrażliwa** | *Kto jest najbardziej zagrożony i gdzie muszę być pierwszy?* | Lakehouse, indeksy wrażliwości i zagrożenia życia, optymalizacja rozstawienia, **Fabric App**, Activator |
| [`ol-infrastruktura-krytyczna`](../ol-infrastruktura-krytyczna/) | **Infrastruktura krytyczna — efekt domina** | *Jeśli ten obiekt padnie, co się stanie i ile mam czasu?* | Lakehouse (graf 11 systemów IK), Eventstream, Eventhouse/KQL, silnik kaskady, Power BI, **Fabric App**, Activator, Data Agent |
| [`ol-spo-copilot`](../ol-spo-copilot/) | **SPO Copilot — asystent procedur** | *Co mam zrobić w ciągu najbliższych 30 minut i kto to podpisuje?* | Lakehouse (korpus + indeks RAG), Eventstream, Eventhouse/KQL, notatniki (TF-IDF, ewaluacja), model semantyczny, Power BI, Activator, Data Agent, **Fabric App** |

### Stan realizacji (2026-07-31)

| Repozytorium | Dane | Modele/analityka | Dokumentacja demo | Status |
|---|---|---|---|---|
| `ol-cop24` | 578 tys. rekordów zdarzeń, 120 wodowskazów, 2477 gmin | Krajowy Indeks Sytuacji, rekomendacje eskalacji | 93 KB | ✅ gotowe |
| `ol-siatka-bezpieczenstwa` | siatka 1000 komórek, 16 SPO, 106 deklaracji gotowości | silnik aktywacji, analiza luk, graf odpowiedzialności | 81 KB | ✅ gotowe |
| `ol-zasoby-logistyka` | 60 magazynów, 400 punktów przyjęcia, 16 901 pozycji transportów | optymalizacja przydziału: **4,27 h → 1,70 h** | 114 KB | ✅ gotowe |
| `ol-blackout-wrazliwi` | 735 602 zdarzeń RT, 900 placówek, 420 agregatów | IWL, IZŻ, rozstawienie: **13,1% → 36,7% pokrycia** | 116 KB | ✅ gotowe |
| `ol-infrastruktura-krytyczna` | 2106 obiektów IK, 6552 zależności, 659 178 zdarzeń RT | silnik kaskady, SPOF, what-if: **−24% skutków wtórnych** | 92 KB | ✅ gotowe |
| `ol-spo-copilot` | 16 SPO / 155 kroków, 513 fragmentów korpusu, 16 608 zdarzeń | RAG: top-1 **90,6%**; SLA **76,1%**; jedna blokada **201 razy w 4 lata** | 103 KB | ✅ gotowe |

Pozostałe pomysły (6 scenariuszy) — [`BACKLOG.md`](BACKLOG.md).
Wspólne konwencje merytoryczne i techniczne — [`CONVENTIONS.md`](CONVENTIONS.md).

### Wdrożenie na Fabric (2026-08-06)

Wszystkie sześć scenariuszy działa na pojemności `fcdemo` (F8, West Europe), każdy
w osobnym obszarze roboczym. Każdy ma wdrożoną aplikację Fabric App (Rayfin) z jasną
paletą rządową i zapisem do własnej bazy.

| Repozytorium | Fabric App | Adres |
|---|---|---|
| `ol-cop24` | Pulpit RZZK | https://key-horn-c1ee0f1637-westeurope.webapp.fabricapps.net |
| `ol-siatka-bezpieczenstwa` | Pulpit koordynacji | https://keen-ore-908e20772e-westeurope.webapp.fabricapps.net |
| `ol-zasoby-logistyka` | Pulpit zasobów | https://trim-cove-aca76ba030-westeurope.webapp.fabricapps.net |
| `ol-blackout-wrazliwi` | Pulpit Tarcza | https://maple-gulf-3321fb8cc7-westeurope.webapp.fabricapps.net |
| `ol-infrastruktura-krytyczna` | Symulator kaskad IK | https://grand-coast-b2b8efb506-westeurope.webapp.fabricapps.net |
| `ol-spo-copilot` | Asystent SPO | https://tangy-poppy-03a3300f0e-westeurope.webapp.fabricapps.net |

Szczegóły wdrożenia — `DEPLOYMENT_STATUS.md` w każdym repozytorium. Kontrast barw we
wszystkich aplikacjach sprawdza [`tools/audit_contrast.py`](tools/audit_contrast.py)
(0 par poniżej progu WCAG 4,5:1).

Każdy scenariusz ma też Data Agenta („Zapytaj o dane") podpiętego do Lakehouse,
Eventhouse i modelu semantycznego. Instrukcja systemowa każdego agenta jest składana
ze specyfikacji `ai/DATA_AGENT.md` w jego repozytorium, więc zmiana specyfikacji wymaga
ponownego uruchomienia `deploy/create_data_agent.py` — dokumentacja i wdrożenie nie
rozjeżdżają się w czasie.

| Repozytorium | Data Agent | Podpięte źródła (tabel) |
|---|---|---|
| `ol-cop24` | `agent_cop24` | Lakehouse 21, Eventhouse 16, model 20 |
| `ol-siatka-bezpieczenstwa` | `agent_siatka_bezpieczenstwa` | Lakehouse 13, Eventhouse 10, model 16 |
| `ol-zasoby-logistyka` | `agent_zasoby_logistyka` | Lakehouse 21, Eventhouse 15, model 21 |
| `ol-blackout-wrazliwi` | `agent_blackout_wrazliwi` | Lakehouse 24, Eventhouse 17, model 24 |
| `ol-infrastruktura-krytyczna` | `agent_infrastruktura_krytyczna` | Lakehouse 14, Eventhouse 5, model 19 |
| `ol-spo-copilot` | `OL_SPO_DataAgent` | Lakehouse 11, Eventhouse 10, model 13 |

Funkcje KQL są w każdym przypadku zweryfikowane, ale opisane w podpowiedzi źródła zamiast
podpięte jako elementy: backend Data Agenta odrzuca elementy typu `kusto.functions`, mimo
że schemat definicji je dopuszcza.

**Do przeklikania przez człowieka:** logowanie brokerem Fabric i zapis wiersza przez
formularz. Sprawdzone automatycznie (HTTP 200, serwowanie sceny, paleta w CSS), ale
ścieżka zapisu nie została wykonana ręcznie od końca do końca w żadnej z aplikacji.
Osobno: **publikacja Data Agentów** z wersji roboczej do produkcyjnej — API Fabric tego
kroku nie udostępnia, trzeba go kliknąć w portalu.

---

## 🧭 Jak to się układa w jedną opowieść

```
        ZAGROŻENIE (KPZK: 20 zagrożeń, matryca ryzyka)
                        │
   ┌────────────────────┼────────────────────┐
   │                    │                    │
COP-24              SIATKA               ZASOBY
"co się dzieje"    "kto działa"        "czym działamy"
   │                    │                    │
   ├────────────────────┼────────────────────┤
   │                    │                    │
   │          INFRASTRUKTURA KRYTYCZNA       │
   │          "co padnie następne"           │
   │                    │                    │
   └────────────────────┼────────────────────┘
                        │
                 LUDNOŚĆ WRAŻLIWA
                 "kogo chronimy najpierw"
```

- **COP-24** odpowiada na pytanie *sytuacyjne* i uruchamia eskalację (gmina → powiat → wojewoda → minister wiodący → RZZK).
- **Siatka Bezpieczeństwa** zamienia decyzję o eskalacji w konkretne zadania dla działów administracji (fazy R i O, moduły zadaniowe).
- **Zasoby** odpowiadają na pytanie o siły i środki oraz decyzję o uruchomieniu rezerw (SPO-2).
- **Infrastruktura krytyczna** dokłada wymiar *przewidywania*: zamienia obraz bieżący w prognozę skutków wtórnych i wskazuje, gdzie inwestycja realnie zmniejsza ryzyko (SPO-10).
- **Ludność wrażliwa** przenosi całość z poziomu administracji (ZK) na poziom człowieka (OL).

Każde repozytorium działa samodzielnie, ale wszystkie używają tej samej geografii
(syntetyczny TERYT), tego samego katalogu zagrożeń (Z01–Z20) i tych samych 16 SPO,
więc można je pokazywać jako jedną, spójną narrację lub osobno.

---

## 🎬 Scenariusze zdarzeń

| Oś | Zdarzenie | Repozytoria |
|---|---|---|
| **POWÓDŹ WRZESIEŃ** (D-3…D+10) | Ekstremalne opady w Sudetach, fala na Nysie Kłodzkiej i Odrze: Kłodzko → Nysa → Opole → Wrocław. Zagrożenia towarzyszące: Z07 energetyka, Z12 telekomunikacja, Z20 dezinformacja | `ol-cop24`, `ol-siatka-bezpieczenstwa`, `ol-zasoby-logistyka`, `ol-infrastruktura-krytyczna`, `ol-spo-copilot` |
| **MRÓZ STYCZEŃ** (D-2…D+7) | Oblodzenie i kaskadowa awaria sieci przy -18 °C w kilku województwach | `ol-blackout-wrazliwi` |

---

## 🚀 Uruchomienie

Każde repozytorium zawiera:

- `README.md` — cel, architektura, uruchomienie
- `DEMO_SCRIPT.md` — **narracja demo** (role, oś czasu, co mówić, co klikać, wow moments, plan B)
- `SETUP_FABRIC.md` — krok po kroku w Microsoft Fabric + lista kontrolna
- `DATA_MODEL.md` — słownik danych
- `generate_datasets.py` — generator danych syntetycznych (`seed=42`, powtarzalny)
- `simulate_realtime.py` — symulator strumienia do Eventstream (`--dry-run` działa offline)
- `kql/`, `notebooks/`, `semantic-model/`, `activator/`, `fabric-app/`

Typowa kolejność:

```powershell
cd C:\repos\OchronaLudnosci\<repo>
pip install -r requirements.txt
python generate_datasets.py
python simulate_realtime.py --dry-run --speed 60
```

Następnie wg `SETUP_FABRIC.md`: workspace → Lakehouse/Eventhouse → KQL → notebooki
→ model semantyczny i raport → Activator → Data Agent → Fabric App.

---

## 🔐 Zasady

- Zero prawdziwych danych osobowych; wszystkie rejestry osób są fikcyjne i pseudonimowane.
- Brak poświadczeń w repozytoriach (`.env` w `.gitignore`, `config.example.json` jako wzorzec).
- W scenariuszach dotykających danych wrażliwych opisano podejście *privacy-by-design*
  (agregacja, minimalizacja, RLS, etykiety wrażliwości) — patrz `ETHICS_AND_PRIVACY.md`
  w `ol-blackout-wrazliwi`.
