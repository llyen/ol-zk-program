# BACKLOG — pozostałe scenariusze demo (nierealizowane w pierwszej turze)

Program: **Ochrona Ludności i Zarządzanie Kryzysowe na Microsoft Fabric**
Status na 2026-07-31. W realizacji: scenariusze **1, 4, 7, 12** (osobne repozytoria).

Poniżej scenariusze odłożone — opis wystarczający, by w każdej chwili uruchomić je jako kolejne repozytorium.

---

## 2. Matryca Ryzyka Live (KPZK)

**Problem:** matryca ryzyka w KPZK (prawdopodobieństwo × skutki dla 20 zagrożeń) jest przeglądana cyklicznie, nie w czasie rzeczywistym. Decydent nie widzi, że ryzyko suszy rośnie od 6 tygodni.

**Rozwiązanie:** dynamiczne przeliczanie pozycji każdego z 20 zagrożeń w matrycy na podstawie bieżących wskaźników (hydrologia, temperatura, stan sieci, incydenty cyber, wskaźniki epidemiczne, ceny/dostawy paliw, aktywność dezinformacyjna).

**Fabric:** Lakehouse (wskaźniki), Notebook (model scoringowy + prognoza 7/30 dni), model semantyczny, Power BI z animowaną matrycą w czasie, Activator (alert przy zmianie kategorii ryzyka), Data Agent („dlaczego ryzyko powodzi wzrosło?").

**Dane syntetyczne:** 3 lata historii wskaźników dziennych dla 20 zagrożeń, sezonowość, 5–6 wstrzykniętych epizodów kryzysowych.

**Wow moment:** zagrożenie przesuwa się na oczach widza z pola żółtego do czerwonego, a system tłumaczy dlaczego i wskazuje właściwe SPO.

**Szacunek pracochłonności:** M (5–8 dni).

---

## 3. Powódź — Ewakuacja i Zasoby (moduł ewakuacyjny)

**Problem:** kogo ewakuować, w jakiej kolejności, jaką trasą, dokąd — przy zmieniającej się przejezdności dróg i rosnącym zasięgu zalania.

**Rozwiązanie:** planer ewakuacji: strefy zagrożenia z prognozy hydrologicznej → populacja w strefie → przypisanie do punktów przyjęcia z uwzględnieniem pojemności i tras → harmonogram transportu → karta ewakuacji dla mieszkańca.

**Fabric:** Lakehouse, Notebook (optymalizacja przydziału i tras), Real-Time Dashboard postępu ewakuacji, **Fabric App „Karta ewakuacji"** (rejestracja osoby, przypisanie miejsca, odnalezienie bliskich), Activator.

**Uwaga:** częściowo pokryty przez repozytoria `ol-cop24` (obraz sytuacji) i `ol-zasoby-logistyka` (punkty przyjęcia). Do realizacji jako pogłębienie wątku „człowiek".

**Szacunek:** L (8–12 dni).

---

## 5. SPO Copilot — asystent procedur

**Problem:** 16 Standardowych Procedur Operacyjnych plus procedury resortowe i wojewódzkie. W kryzysie oficer dyżurny musi w minutę wiedzieć, którą uruchomić i jakie są kolejne kroki.

**Rozwiązanie:** asystent RAG nad korpusem procedur (SPO, KPZK, wojewódzkie plany ZK, plany OL) + workflow checklisty z rejestrem wykonania i dziennikiem decyzji (ślad audytowy dla późniejszego rozliczenia i lessons learned).

**Fabric:** Lakehouse (dokumenty + indeks wektorowy), AI Skill / Data Agent, AI Functions (streszczenia, ekstrakcja kroków), Fabric App (checklista + dziennik), Power BI (czasy realizacji kroków).

**Dane syntetyczne:** fikcyjne, ale realistyczne treści 16 SPO z krokami, rolami, SLA i wzorami dokumentów.

**Wow moment:** pytanie głosem „mamy skażenie chemiczne w porcie, co robimy?" → asystent podaje właściwą SPO, kroki, odpowiedzialnych i generuje listę telefoniczną.

**Szacunek:** M (5–8 dni). **Rekomendacja: wysoki priorytet w drugiej turze.**

---

## 6. Infrastruktura Krytyczna — efekt domina

**Problem:** systemy IK są współzależne. Awaria energetyczna zatrzymuje przepompownie wody, stacje bazowe, szpitale, sygnalizację. Nikt nie ma jednego modelu tych zależności.

**Rozwiązanie:** graf zależności infrastruktury krytycznej + symulacja kaskad: „wyłącz węzeł X" → lista skutków wtórnych i trzeciego rzędu, populacja dotknięta, czas do wystąpienia skutku.

**Fabric:** Lakehouse (węzły i krawędzie grafu), Notebook (propagacja kaskady, centralność węzłów, identyfikacja pojedynczych punktów awarii), Power BI (mapa + drzewo skutków), Data Agent, scenariusze what-if. Powiązanie z SPO-10.

**Dane syntetyczne:** ~2000 obiektów IK w 11 systemach (energia, gaz, paliwa, woda, telekomunikacja, transport, zdrowie, finanse, żywność, ratownictwo, administracja) z zależnościami.

**Wow moment:** kliknięcie w jedną stację i natychmiastowa odpowiedź „bez prądu 412 tys. osób, 3 szpitale na agregatach z autonomią 48h, 14 przepompowni wody — woda przestanie płynąć za 6 godzin".

**Szacunek:** L (8–12 dni). **Rekomendacja: wysoki priorytet — bardzo mocny wizualnie.**

---

## 8. Dezinformacja / OSINT

**Problem:** zagrożenie Z20 z KPZK. W kryzysie fałszywe komunikaty („woda skażona", „tama pękła") potrafią wywołać panikę szybciej niż samo zdarzenie.

**Rozwiązanie:** monitoring narracji: klasyfikacja treści, wykrywanie skoordynowanych kampanii i kont nieautentycznych, mapowanie narracji na obszary geograficzne, rekomendacja treści sprostowania (SPO-3).

**Fabric:** Eventstream (symulowany strumień mediów i social), Eventhouse, AI Functions (klasyfikacja, sentyment, ekstrakcja tematów, wykrywanie duplikatów), Real-Time Dashboard, Activator, Data Agent.

**Uwaga:** wymaga ostrożnej komunikacji — demo musi jasno oddzielać wykrywanie dezinformacji od jakiejkolwiek formy cenzury; nacisk na szybkość rzetelnej informacji.

**Szacunek:** M (5–8 dni).

---

## 9. System ostrzegania ludności (RSO / Alert RCB)

**Problem:** wysłanie alertu to nie to samo co dotarcie alertu. Brak pomiaru skuteczności i doboru kanału do odbiorcy.

**Rozwiązanie:** segmentacja geograficzna odbiorców, wybór kanału (SMS, RSO, syreny, radio, aplikacja, obwoluta sołecka), pomiar dostarczenia i reakcji, testy wariantów treści, wykrywanie „martwych stref" komunikacyjnych.

**Fabric:** Eventstream (zdarzenia wysyłki i dostarczenia), Eventhouse, Power BI (skuteczność per gmina i kanał), AI Functions (generowanie i upraszczanie treści komunikatu, tłumaczenia — także dla obcokrajowców), Activator.

**Uwaga:** częściowo pokryte w `ol-blackout-wrazliwi` (ekran SPO-3). Pełny scenariusz = pogłębienie.

**Szacunek:** S/M (3–6 dni).

---

## 10. Ćwiczenia i lessons learned

**Problem:** po każdym zdarzeniu i ćwiczeniu powstają raporty, których nikt nie analizuje ilościowo. Nie wiadomo, czy gotowość rośnie.

**Rozwiązanie:** hurtownia zdarzeń i ćwiczeń: czasy reakcji na każdym poziomie, wąskie gardła, powtarzające się rekomendacje, scorecard gotowości gmin/powiatów/województw, automatyczne streszczanie raportów po-zdarzeniowych i grupowanie wniosków.

**Fabric:** Lakehouse/Warehouse, Notebook (analiza czasów, klastrowanie wniosków), AI Functions (streszczenia, tagowanie), Power BI scorecard, Data Agent („jakie wnioski powtarzają się od trzech lat?").

**Wow moment:** „ta sama rekomendacja o łączności między PSP a energetyką pojawia się w 14 raportach od 2019 r. i nigdy nie została wdrożona".

**Szacunek:** M (5–8 dni).

---

## 11. Zagrożenia hybrydowe — fuzja sygnałów

**Problem:** zagrożenie Z04. Pojedyncze incydenty (uszkodzony kabel, dron nad obiektem, incydent cyber, presja migracyjna, awaria) są obsługiwane osobno przez różne służby. Wzorzec ataku widać dopiero po zestawieniu.

**Rozwiązanie:** korelacja czasowo-przestrzenna zdarzeń z wielu domen, scoring „prawdopodobieństwo skoordynowanego działania", automatyczne budowanie osi czasu incydentu złożonego i propozycja eskalacji do Zespołu ds. Incydentów Krytycznych (SPO-16).

**Fabric:** Eventstream (wiele domen), Eventhouse (korelacje KQL, detekcja anomalii), Notebook (graf powiązań), Real-Time Dashboard, Activator, Data Agent.

**Szacunek:** L (8–12 dni). **Rekomendacja: bardzo mocny scenariusz dla odbiorcy MON/MSWiA/RCB.**

---

## Rekomendowana kolejność drugiej tury

1. **#6 Infrastruktura krytyczna — efekt domina** (wysoka wartość wizualna, naturalna kontynuacja COP-24)
2. **#5 SPO Copilot** (najkrótsza droga do „AI, którą decydent rozumie")
3. **#11 Zagrożenia hybrydowe** (najsilniejszy przekaz dla odbiorcy bezpieczeństwa państwa)
4. **#2 Matryca ryzyka live** (spina całość na poziomie strategicznym)

---

*Wszystkie scenariusze zakładają wyłącznie dane syntetyczne i mają charakter demonstracyjny.*
