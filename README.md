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

### Stan realizacji (2026-07-31)

| Repozytorium | Dane | Modele/analityka | Dokumentacja demo | Status |
|---|---|---|---|---|
| `ol-cop24` | 578 tys. rekordów zdarzeń, 120 wodowskazów, 2477 gmin | Krajowy Indeks Sytuacji, rekomendacje eskalacji | 93 KB | ✅ gotowe |
| `ol-siatka-bezpieczenstwa` | siatka 1000 komórek, 16 SPO, 106 deklaracji gotowości | silnik aktywacji, analiza luk, graf odpowiedzialności | 81 KB | ✅ gotowe |
| `ol-zasoby-logistyka` | 60 magazynów, 400 punktów przyjęcia, 16 901 pozycji transportów | optymalizacja przydziału: **4,27 h → 1,70 h** | 114 KB | ✅ gotowe |
| `ol-blackout-wrazliwi` | 735 602 zdarzeń RT, 900 placówek, 420 agregatów | IWL, IZŻ, rozstawienie: **13,1% → 36,7% pokrycia** | 116 KB | ✅ gotowe |

Pozostałe pomysły (8 scenariuszy) — [`BACKLOG.md`](BACKLOG.md).
Wspólne konwencje merytoryczne i techniczne — [`CONVENTIONS.md`](CONVENTIONS.md).

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
   └────────────────────┼────────────────────┘
                        │
                 LUDNOŚĆ WRAŻLIWA
                 "kogo chronimy najpierw"
```

- **COP-24** odpowiada na pytanie *sytuacyjne* i uruchamia eskalację (gmina → powiat → wojewoda → minister wiodący → RZZK).
- **Siatka Bezpieczeństwa** zamienia decyzję o eskalacji w konkretne zadania dla działów administracji (fazy R i O, moduły zadaniowe).
- **Zasoby** odpowiadają na pytanie o siły i środki oraz decyzję o uruchomieniu rezerw (SPO-2).
- **Ludność wrażliwa** przenosi całość z poziomu administracji (ZK) na poziom człowieka (OL).

Każde repozytorium działa samodzielnie, ale wszystkie używają tej samej geografii
(syntetyczny TERYT), tego samego katalogu zagrożeń (Z01–Z20) i tych samych 16 SPO,
więc można je pokazywać jako jedną, spójną narrację lub osobno.

---

## 🎬 Scenariusze zdarzeń

| Oś | Zdarzenie | Repozytoria |
|---|---|---|
| **POWÓDŹ WRZESIEŃ** (D-3…D+10) | Ekstremalne opady w Sudetach, fala na Nysie Kłodzkiej i Odrze: Kłodzko → Nysa → Opole → Wrocław. Zagrożenia towarzyszące: Z07 energetyka, Z12 telekomunikacja, Z20 dezinformacja | `ol-cop24`, `ol-siatka-bezpieczenstwa`, `ol-zasoby-logistyka` |
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
