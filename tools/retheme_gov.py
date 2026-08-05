"""
Sprowadza ciemne pulpity do jasnej konwencji rządowej.

Wzorcem jest `pulpit-koordynacji`, który od początku powstał jasny:
biała karta na `bg-slate-100`, obramowanie `border-slate-200`, `shadow-sm`,
plakietki `bg-*-100 text-*-800 ring-*-600/30`.

Skrypt nie zgaduje. Ma jawną tablicę odwzorowań (prefiks, rodzina, odcień)
i zgłasza każdą klasę koloru, której nie potrafi odwzorować, zamiast
zostawiać ją po cichu — nieodwzorowana klasa to jasny tekst na jasnym tle.

Uruchomienie:
    python retheme_gov.py            # tylko raport, bez zapisu
    python retheme_gov.py --apply
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(r"C:\repos\OchronaLudnosci")

# Aplikacje zbudowane w ciemnym motywie. `pulpit-koordynacji` jest pominięty
# celowo — jest już jasny i służy za wzorzec.
DARK_APPS = [
    ROOT / "ol-blackout-wrazliwi" / "fabric-app" / "pulpit-tarcza",
    ROOT / "ol-cop24" / "fabric-app" / "pulpit-rzzk",
    ROOT / "ol-zasoby-logistyka" / "fabric-app" / "pulpit-zasobow",
]

SUFFIXES = (".tsx", ".ts", ".css")

CLASS_RX = re.compile(
    r"\b(?P<prefix>bg|text|ring|border|divide|from|via|to|fill|stroke|accent|shadow|"
    r"outline|placeholder|decoration)-"
    r"(?P<color>slate|gray|zinc|neutral|stone|sky|cyan|blue|indigo|violet|purple|"
    r"fuchsia|pink|rose|red|orange|amber|yellow|lime|green|emerald|teal)-"
    r"(?P<shade>950|900|800|700|600|500|400|300|200|100|50)"
    r"(?P<op>/\d+)?\b"
)

# ---------------------------------------------------------------------------
# Odwzorowanie
# ---------------------------------------------------------------------------

# Powierzchnie. Ciemny motyw budował głębię przez coraz jaśniejsze szarości;
# jasny robi to odwrotnie — biała karta odcina się od szarej strony.
# Przezroczystość jest tu porzucana: na jasnym tle warstwy `/60` dają
# wyprany, nieczytelny wynik.
SURFACE = {
    ("bg", "slate", "950"): "bg-slate-100",   # tło strony
    ("bg", "slate", "900"): "bg-white",       # karta
    ("bg", "slate", "800"): "bg-slate-50",    # nagłówek tabeli, plakietka
    ("bg", "slate", "700"): "bg-slate-200",   # tor paska, trzeci poziom
    ("from", "slate", "900"): "from-white",
    ("via", "slate", "900"): "via-white",
    ("to", "slate", "950"): "to-slate-100",
    ("from", "slate", "950"): "from-slate-100",
}

# Tekst. W ciemnym motywie im niższy numer, tym jaśniejszy napis;
# w jasnym kolejność się odwraca.
TEXT = {
    ("text", "slate", "50"): "text-slate-900",
    ("text", "slate", "100"): "text-slate-900",
    ("text", "slate", "200"): "text-slate-900",
    ("text", "slate", "300"): "text-slate-700",
    ("text", "slate", "400"): "text-slate-500",
    ("text", "slate", "500"): "text-slate-500",
    ("text", "slate", "600"): "text-slate-400",
    # Napis na nasyconym przycisku — był ciemny, ma być biały.
    ("text", "slate", "950"): "text-white",
    ("text", "slate", "900"): "text-white",
    ("text", "slate", "800"): "text-white",
    ("text", "slate", "700"): "text-white",
}

# Linie.
LINE = {
    ("ring", "slate", "700"): "ring-slate-200",
    ("ring", "slate", "600"): "ring-slate-300",
    ("ring", "slate", "500"): "ring-slate-300",
    ("ring", "slate", "800"): "ring-slate-200",
    ("border", "slate", "800"): "border-slate-200",
    ("border", "slate", "700"): "border-slate-200",
    ("border", "slate", "600"): "border-slate-300",
    ("divide", "slate", "800"): "divide-slate-200",
    ("divide", "slate", "700"): "divide-slate-200",
}

# Barwa wiodąca. Ciemne pulpity używały błękitu (cyan/sky) jako barwy marki
# i wyróżnienia. Cała ta rodzina idzie na błękit gov `#0052A5`,
# wystawiony jako `--color-gov` w `main.css`.
GOV: dict[tuple[str, str, str], str] = {}
for _pref, _tpl in (
    ("text", "text-gov"),
    ("bg", "bg-gov"),
    ("ring", "ring-gov"),
    ("border", "border-gov"),
    ("accent", "accent-gov"),
    ("fill", "fill-gov"),
    ("stroke", "stroke-gov"),
    ("from", "from-gov"),
    ("to", "to-gov"),
    ("via", "via-gov"),
):
    for _fam in ("cyan", "sky", "indigo", "blue"):
        for _sh in ("200", "300", "400", "500", "600", "700", "800", "900", "950"):
            GOV[(_pref, _fam, _sh)] = _tpl

# Jasne tła plakietek zostają jasne — nie idą na barwę wiodącą.
for _fam in ("cyan", "sky", "indigo", "blue"):
    GOV[("bg", _fam, "50")] = "bg-gov-50"
    GOV[("bg", _fam, "100")] = "bg-gov-50"
    GOV[("text", _fam, "100")] = "text-gov-dark"
    GOV[("text", _fam, "800")] = "text-gov-dark"
    GOV[("text", _fam, "900")] = "text-gov-dark"
    GOV[("from", _fam, "50")] = "from-gov-50"
    GOV[("to", _fam, "50")] = "to-gov-50"

# Barwy sygnalizacyjne. Czerwień, bursztyn, pomarańcz i zieleń niosą
# powagę sytuacji, więc rodziny zostają — zmienia się tylko odcień,
# żeby napis był czytelny na bieli.
SIGNAL_TEXT = {"100": "800", "200": "800", "300": "700", "400": "700", "500": "700"}
SIGNAL: dict[tuple[str, str, str], str] = {}
for _fam in ("red", "rose", "amber", "orange", "emerald", "green", "yellow"):
    _target = "red" if _fam == "rose" else ("emerald" if _fam == "green" else _fam)
    for _from, _to in SIGNAL_TEXT.items():
        SIGNAL[("text", _fam, _from)] = f"text-{_target}-{_to}"
    SIGNAL[("bg", _fam, "500")] = f"bg-{_target}-50"
    SIGNAL[("bg", _fam, "400")] = f"bg-{_target}-400"
    SIGNAL[("ring", _fam, "500")] = f"ring-{_target}-600"
    SIGNAL[("ring", _fam, "600")] = f"ring-{_target}-600"
    SIGNAL[("border", _fam, "500")] = f"border-{_target}-300"

MAPPING: dict[tuple[str, str, str], str] = {}
for _table in (GOV, SIGNAL, SURFACE, TEXT, LINE):
    MAPPING.update(_table)

# Klasy, które w jasnym motywie są już poprawne i mają zostać nietknięte:
# nasycone przyciski, jasne plakietki szablonu.
KEEP = {
    ("bg", "red", "600"), ("bg", "red", "700"), ("bg", "red", "100"), ("bg", "red", "50"),
    ("bg", "emerald", "600"), ("bg", "emerald", "700"), ("bg", "emerald", "100"),
    ("bg", "emerald", "50"), ("bg", "amber", "100"), ("bg", "amber", "50"),
    ("bg", "orange", "50"), ("bg", "slate", "50"), ("bg", "slate", "500"),
    ("bg", "slate", "100"), ("bg", "slate", "200"), ("bg", "slate", "300"),
    ("bg", "gray", "50"), ("bg", "gray", "100"),
    ("text", "red", "600"), ("text", "red", "700"), ("text", "red", "800"),
    ("text", "amber", "700"), ("text", "amber", "800"),
    ("text", "emerald", "600"), ("text", "emerald", "700"), ("text", "emerald", "800"),
    ("text", "orange", "700"), ("text", "orange", "800"),
    ("text", "gray", "900"), ("text", "gray", "600"),
    ("text", "gray", "500"), ("text", "gray", "400"), ("text", "gray", "300"),
    ("border", "slate", "300"), ("border", "slate", "200"), ("border", "slate", "100"),
    ("border", "gray", "300"), ("border", "gray", "200"), ("border", "gray", "100"),
    ("border", "red", "700"), ("border", "emerald", "700"), ("border", "emerald", "200"),
    ("border", "amber", "400"), ("border", "amber", "500"), ("border", "orange", "600"),
    ("ring", "slate", "300"), ("ring", "slate", "200"),
    ("placeholder", "gray", "400"),
}

# Cienie ciemnego motywu nie mają odpowiednika — na jasnym tle robią brud.
SHADOW_DROP = re.compile(
    r"\s*\bshadow-(?:cyan|blue|red|slate|emerald|amber|indigo|sky)-\d{2,3}(?:/\d+)?\b"
)

# Wartości szesnastkowe wpisane wprost w kod.
HEX = {
    "#38bdf8": "#0052a5",  # linia trasy / wyróżnienie
    "#22d3ee": "#0052a5",  # iskierka
    "#0ea5e9": "#0052a5",  # mapa: znacznik
    "#0891b2": "#0052a5",
    "#0e7490": "#00417f",
    "#1d4ed8": "#0052a5",
    "#60a5fa": "#3d7ebf",
    "#dc2626": "#d5233f",  # stan krytyczny — czerwień gov
    "#f87171": "#d5233f",
    "#fb923c": "#c2410c",
    "#f97316": "#c2410c",
    "#facc15": "#a16207",
    "#fbbf24": "#a16207",
    "#f59e0b": "#b45309",
    "#4ade80": "#15803d",
    "#34d399": "#15803d",
    "#a855f7": "#7e22ce",
    # Chrom mapy: ciemne płótno na jasne.
    "#0b1220": "#eef2f7",  # tło mapy
    "#0f172a": "#ffffff",  # tło kafelka / obwódka znacznika
    "#475569": "#c3ced9",  # granice województw
    "#64748b": "#94a3b8",
    "#94a3b8": "#64748b",  # napisy na mapie
    "#cbd5e1": "#334155",
    "#f8fafc": "#0f172a",
    # Granat wzorcowej aplikacji na błękit gov.
    "#0f2a52": "#0052a5",
    "#173a6d": "#00417f",
}
HEX_RX = re.compile("|".join(re.escape(k) for k in HEX), re.IGNORECASE)

# Logo Microsoftu na ekranie logowania zostaje bez zmian.
HEX_SKIP_FILES = {"AuthPage.tsx"}


def retheme_text(text: str, filename: str, unmapped: Counter) -> str:
    def repl(m: re.Match[str]) -> str:
        prefix, color, shade = m.group("prefix"), m.group("color"), m.group("shade")
        op = m.group("op") or ""
        key = (prefix, color, shade)
        if key in KEEP:
            return m.group(0)
        target = MAPPING.get(key)
        if target is None:
            unmapped[f"{prefix}-{color}-{shade}"] += 1
            return m.group(0)
        # Przezroczystość zostaje tylko przy obwódkach i delikatnych tłach,
        # gdzie jest częścią konwencji wzorca (`ring-*-600/30`).
        if op and (prefix == "ring" or target.endswith(("-50", "gov"))):
            return target + op
        return target

    out = CLASS_RX.sub(repl, text)
    out = SHADOW_DROP.sub("", out)
    if filename not in HEX_SKIP_FILES:
        out = HEX_RX.sub(lambda m: HEX[m.group(0).lower()], out)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    unmapped: Counter = Counter()
    changed, scanned = 0, 0

    for app in DARK_APPS:
        src = app / "src"
        if not src.exists():
            print(f"POMINIETO (brak): {src}")
            continue
        for path in sorted(src.rglob("*")):
            if path.suffix not in SUFFIXES or not path.is_file():
                continue
            scanned += 1
            original = path.read_text(encoding="utf-8")
            updated = retheme_text(original, path.name, unmapped)
            if updated != original:
                changed += 1
                if args.apply:
                    path.write_text(updated, encoding="utf-8")

    print(f"Przejrzano plikow: {scanned}")
    print(f"Zmienionych plikow: {changed}{'' if args.apply else ' (proba, bez zapisu)'}")
    if unmapped:
        print("\nKlasy bez odwzorowania (do decyzji recznej):")
        for name, count in unmapped.most_common():
            print(f"  {count:4}  {name}")
    else:
        print("\nKazda klasa koloru ma odwzorowanie.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
