"""
Audyt kontrastu klas Tailwind w aplikacjach Fabric.

Po przemalowaniu z ciemnego motywu na jasną paletę rządową kompilator i testy
nie wykryją jedynego naprawdę groźnego błędu: jasnego napisu na jasnym tle.
Skrypt czyta atrybuty `className`, paruje w każdym z nich barwę tła z barwą
tekstu i liczy kontrast wg WCAG 2.1. Zgłasza pary poniżej 4,5:1 (tekst zwykły).

    python tools/audit_contrast.py            # wszystkie aplikacje
    python tools/audit_contrast.py --min 3.0  # łagodniejszy próg

Ograniczenia (świadome):
* rozpoznaje tylko tło zadeklarowane w tym samym atrybucie co tekst; tło
  odziedziczone z rodzica trzeba sprawdzić okiem,
* pomija klasy warunkowe (`hover:`, `focus:`) — te nie decydują o czytelności
  stanu spoczynkowego.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

APPS = [
    "ol-siatka-bezpieczenstwa/fabric-app/pulpit-koordynacji",
    "ol-cop24/fabric-app/pulpit-rzzk",
    "ol-zasoby-logistyka/fabric-app/pulpit-zasobow",
    "ol-blackout-wrazliwi/fabric-app/pulpit-tarcza",
]

# Paleta Tailwind v4 (podzbiór faktycznie używany) + barwy własne gov.
PALETTE: dict[str, str] = {
    "white": "#ffffff",
    "black": "#000000",
    "transparent": "",
    "gov": "#0052a5",
    "gov-dark": "#00417f",
    "gov-light": "#006cd7",
    "gov-50": "#e8eef7",
    "gov-ink": "#1b1b1b",
    "gov-red": "#d5233f",
}

RAMPS = {
    "slate": ["#f8fafc", "#f1f5f9", "#e2e8f0", "#cbd5e1", "#94a3b8", "#64748b",
              "#475569", "#334155", "#1e293b", "#0f172a", "#020617"],
    "gray": ["#f9fafb", "#f3f4f6", "#e5e7eb", "#d1d5db", "#9ca3af", "#6b7280",
             "#4b5563", "#374151", "#1f2937", "#111827", "#030712"],
    "red": ["#fef2f2", "#fee2e2", "#fecaca", "#fca5a5", "#f87171", "#ef4444",
            "#dc2626", "#b91c1c", "#991b1b", "#7f1d1d", "#450a0a"],
    "orange": ["#fff7ed", "#ffedd5", "#fed7aa", "#fdba74", "#fb923c", "#f97316",
               "#ea580c", "#c2410c", "#9a3412", "#7c2d12", "#431407"],
    "amber": ["#fffbeb", "#fef3c7", "#fde68a", "#fcd34d", "#fbbf24", "#f59e0b",
              "#d97706", "#b45309", "#92400e", "#78350f", "#451a03"],
    "yellow": ["#fefce8", "#fef9c3", "#fef08a", "#fde047", "#facc15", "#eab308",
               "#ca8a04", "#a16207", "#854d0e", "#713f12", "#422006"],
    "green": ["#f0fdf4", "#dcfce7", "#bbf7d0", "#86efac", "#4ade80", "#22c55e",
              "#16a34a", "#15803d", "#166534", "#14532d", "#052e16"],
    "emerald": ["#ecfdf5", "#d1fae5", "#a7f3d0", "#6ee7b7", "#34d399", "#10b981",
                "#059669", "#047857", "#065f46", "#064e3b", "#022c22"],
    "teal": ["#f0fdfa", "#ccfbf1", "#99f6e4", "#5eead4", "#2dd4bf", "#14b8a6",
             "#0d9488", "#0f766e", "#115e59", "#134e4a", "#042f2e"],
    "cyan": ["#ecfeff", "#cffafe", "#a5f3fc", "#67e8f9", "#22d3ee", "#06b6d4",
             "#0891b2", "#0e7490", "#155e75", "#164e63", "#083344"],
    "sky": ["#f0f9ff", "#e0f2fe", "#bae6fd", "#7dd3fc", "#38bdf8", "#0ea5e9",
            "#0284c7", "#0369a1", "#075985", "#0c4a6e", "#082f49"],
    "blue": ["#eff6ff", "#dbeafe", "#bfdbfe", "#93c5fd", "#60a5fa", "#3b82f6",
             "#2563eb", "#1d4ed8", "#1e40af", "#1e3a8a", "#172554"],
    "indigo": ["#eef2ff", "#e0e7ff", "#c7d2fe", "#a5b4fc", "#818cf8", "#6366f1",
               "#4f46e5", "#4338ca", "#3730a3", "#312e81", "#1e1b4b"],
    "violet": ["#f5f3ff", "#ede9fe", "#ddd6fe", "#c4b5fd", "#a78bfa", "#8b5cf6",
               "#7c3aed", "#6d28d9", "#5b21b6", "#4c1d95", "#2e1065"],
    "purple": ["#faf5ff", "#f3e8ff", "#e9d5ff", "#d8b4fe", "#c084fc", "#a855f7",
               "#9333ea", "#7e22ce", "#6b21a8", "#581c87", "#3b0764"],
    "fuchsia": ["#fdf4ff", "#fae8ff", "#f5d0fe", "#f0abfc", "#e879f9", "#d946ef",
                "#c026d3", "#a21caf", "#86198f", "#701a75", "#4a044e"],
    "pink": ["#fdf2f8", "#fce7f3", "#fbcfe8", "#f9a8d4", "#f472b6", "#ec4899",
             "#db2777", "#be185d", "#9d174d", "#831843", "#500724"],
    "rose": ["#fff1f2", "#ffe4e6", "#fecdd3", "#fda4af", "#fb7185", "#f43f5e",
             "#e11d48", "#be123c", "#9f1239", "#881337", "#4c0519"],
    "lime": ["#f7fee7", "#ecfccb", "#d9f99d", "#bef264", "#a3e635", "#84cc16",
             "#65a30d", "#4d7c0f", "#3f6212", "#365314", "#1a2e05"],
    "stone": ["#fafaf9", "#f5f5f4", "#e7e5e4", "#d6d3d1", "#a8a29e", "#78716c",
              "#57534e", "#44403c", "#292524", "#1c1917", "#0c0a09"],
    "zinc": ["#fafafa", "#f4f4f5", "#e4e4e7", "#d4d4d8", "#a1a1aa", "#71717a",
             "#52525b", "#3f3f46", "#27272a", "#18181b", "#09090b"],
    "neutral": ["#fafafa", "#f5f5f5", "#e5e5e5", "#d4d4d4", "#a3a3a3", "#737373",
                "#525252", "#404040", "#262626", "#171717", "#0a0a0a"],
}

SHADES = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]

for name, ramp in RAMPS.items():
    for shade, hexv in zip(SHADES, ramp):
        PALETTE[f"{name}-{shade}"] = hexv

CLASSNAME_RE = re.compile(r'className\s*=\s*(?:"([^"]*)"|\{`([^`]*)`\}|\{([^}]*)\})', re.S)
TOKEN_RE = re.compile(
    r'\b(bg|text)-([a-z]+(?:-\d{2,3})?|white|black|gov(?:-[a-z0-9]+)?)(?:/(\d{1,3}))?\b'
)

# Klasy `text-*`, które nie są barwą, tylko rozmiarem lub układem.
NOT_A_COLOR = {
    "xs", "sm", "base", "lg", "xl", "left", "right", "center", "justify",
    "wrap", "nowrap", "balance", "pretty", "ellipsis", "clip", "transparent",
}


def luminance(hexv: str) -> float:
    r, g, b = (int(hexv[i : i + 2], 16) / 255 for i in (1, 3, 5))

    def lin(c: float) -> float:
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def contrast(a: str, b: str) -> float:
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def blend_on_white(hexv: str, alpha: int) -> str:
    """
    Barwa z modyfikatorem przezroczystości leży faktycznie na tle strony.
    Tło strony jest jasne, więc `bg-gov/15` to nie granat, tylko jego blady
    odcień — bez tego przeliczenia audyt zgłaszałby fałszywe alarmy.
    """
    a = alpha / 100
    out = "#"
    for i in (1, 3, 5):
        c = int(hexv[i : i + 2], 16)
        out += f"{round(c * a + 255 * (1 - a)):02x}"
    return out


def scan_file(path: Path, min_ratio: float) -> list[str]:
    src = path.read_text(encoding="utf-8")
    problems: list[str] = []
    for match in CLASSNAME_RE.finditer(src):
        blob = next(g for g in match.groups() if g is not None)
        # Warianty stanu nie decydują o czytelności stanu spoczynkowego.
        blob = re.sub(r"\b(?:hover|focus|active|group-hover|disabled):\S+", " ", blob)
        bg: str | None = None
        fg: str | None = None
        for kind, value, alpha in TOKEN_RE.findall(blob):
            if value in NOT_A_COLOR:
                continue
            hexv = PALETTE.get(value)
            if not hexv:
                continue
            if alpha:
                hexv = blend_on_white(hexv, int(alpha))
            if kind == "bg" and bg is None:
                bg = hexv
            elif kind == "text" and fg is None:
                fg = hexv
        if bg and fg:
            ratio = contrast(bg, fg)
            if ratio < min_ratio:
                line = src[: match.start()].count("\n") + 1
                problems.append(f"{path.name}:{line}  {ratio:.2f}:1  tlo {bg} / tekst {fg}")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--min", type=float, default=4.5, help="prog kontrastu WCAG")
    args = ap.parse_args()

    total = 0
    for app in APPS:
        src_dir = ROOT.parent / app / "src"
        if not src_dir.exists():
            print(f"[pominieto] brak katalogu {src_dir}")
            continue
        found: list[str] = []
        for path in sorted(src_dir.rglob("*.tsx")):
            found.extend(scan_file(path, args.min))
        total += len(found)
        head = f"{app.split('/')[-1]}: {len(found)} par ponizej {args.min}:1"
        print(head)
        print("-" * len(head))
        for line in found:
            print("  " + line)
        print()

    print(f"Razem: {total}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
