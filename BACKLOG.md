# BACKLOG — pozostałe scenariusze demo (nierealizowane)
Program: **Ochrona Ludności i Zarządzanie Kryzysowe na Microsoft Fabric**
Status na 2026-07-31. Zrealizowane: scenariusze **1, 4, 5, 6, 7, 12** (osobne repozytoria).

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

## ~~5. SPO Copilot — asystent procedur~~ — ZREALIZOWANY

> Zrealizowany jako repozytorium [`ol-spo-copilot`](../ol-spo-copilot/): korpus 16 SPO
> (155 kroków) plus plany wojewódzkie, plany OL i KPZK — 49 dokumentów / 513 fragmentów,
> retriever TF-IDF z routingiem pytanie → procedura (top-1 90,6%, top-3 93,8%, MRR 0,932),
> karta odpowiedzi z checklistą i cytowaniami, dziennik decyzji oraz analityka czasów
> normatywnych (dotrzymanie 76,1%) i powtarzających się blokad
> (jedna przyczyna — 201 wystąpień w 4 lata).

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

1. **#11 Zagrożenia hybrydowe** (najsilniejszy przekaz dla odbiorcy bezpieczeństwa państwa)
2. **#2 Matryca ryzyka live** (spina całość na poziomie strategicznym)
3. **#9 System ostrzegania ludności** (domyka wątek „komunikat do obywatela")

> **#6 Infrastruktura krytyczna — efekt domina** został zrealizowany jako repozytorium
> [`ol-infrastruktura-krytyczna`](../ol-infrastruktura-krytyczna/): 2106 obiektów IK w 11 systemach,
> 6552 zależności, silnik propagacji kaskady, ranking pojedynczych punktów awarii i porównanie
> wariantów wzmocnienia.
>
> **#5 SPO Copilot** został zrealizowany jako repozytorium
> [`ol-spo-copilot`](../ol-spo-copilot/) — szczegóły przy pozycji nr 5 powyżej.

---

*Wszystkie scenariusze zakładają wyłącznie dane syntetyczne i mają charakter demonstracyjny.*
