# -*- coding: utf-8 -*-
"""Gaply partner-offerte-generator.

Gebruik:  python3 generate_offerte.py config.json output.pdf

Genereert een offerte-PDF (max 3 A4) met een vaste 7-sectiestructuur, in de
huisstijl van de PARTNER (kleuren en logo uit het "branding"-blok in de
config). Alle inhoud komt uit config.json; zie references/voorbeeld-config.json
voor een compleet ingevuld voorbeeld.

Vereist: reportlab (pip install reportlab --break-system-packages).
Tekst in paragrafen/cellen mag ReportLab-XML bevatten (<b>, <i>, <font>).
Gebruik &amp; voor een ampersand.
"""
import json
import sys

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)

PAGE_W, PAGE_H = A4
M = 20 * mm

# Defaults (Gaply-huisstijl) als het branding-blok een veld niet invult
DEFAULTS = {
    "kleur_donker": "#15151F",
    "kleur_primair": "#00C39B",
    "kleur_primair_licht": "#E2F8F1",
    "kleur_signaal": "#E5147E",
}


def main(config_path, out_path):
    with open(config_path) as f:
        cfg = json.load(f)
    meta = cfg["meta"]
    br = cfg.get("branding", {})

    DARK = HexColor(br.get("kleur_donker", DEFAULTS["kleur_donker"]))
    PRIM = HexColor(br.get("kleur_primair", DEFAULTS["kleur_primair"]))
    PRIMBG = HexColor(br.get("kleur_primair_licht", DEFAULTS["kleur_primair_licht"]))
    SIGN = HexColor(br.get("kleur_signaal", DEFAULTS["kleur_signaal"]))
    prim_hex = br.get("kleur_primair", DEFAULTS["kleur_primair"])
    sign_hex = br.get("kleur_signaal", DEFAULTS["kleur_signaal"])
    GREY = HexColor("#5A5A66")
    LINE = HexColor("#DDDDE2")
    LIGHT = HexColor("#F4F4F7")
    REDBG = HexColor("#FBE9EE")
    partner_naam = br.get("partner_naam", "Gaply")

    def header_footer(canv, doc):
        canv.saveState()
        # Partnerlogo of partnernaam linksboven
        x, y = M, PAGE_H - 16 * mm
        plogo = br.get("partner_logo")
        if plogo:
            lw = br.get("partner_logo_breedte_mm", 30) * mm
            lh = lw * br.get("partner_logo_ratio", 0.3)
            canv.drawImage(plogo, x, y - 2 * mm, width=lw, height=lh,
                           preserveAspectRatio=True, mask="auto")
        else:
            canv.setFillColor(DARK)
            canv.setFont("Helvetica-Bold", 15)
            canv.drawString(x, y, partner_naam)
        # Optioneel klantlogo rechtsboven (PNG, liefst met transparantie)
        logo = meta.get("klant_logo")
        if logo:
            lw = meta.get("klant_logo_breedte_mm", 26) * mm
            lh = lw * meta.get("klant_logo_ratio", 0.5)
            canv.drawImage(logo, PAGE_W - M - lw, PAGE_H - 20 * mm, width=lw,
                           height=lh, preserveAspectRatio=True, mask="auto")
        canv.setStrokeColor(SIGN)
        canv.setLineWidth(1.2)
        canv.line(M, PAGE_H - 22 * mm, PAGE_W - M, PAGE_H - 22 * mm)
        canv.setFont("Helvetica", 8)
        canv.setFillColor(GREY)
        canv.drawCentredString(PAGE_W / 2, 11 * mm,
                               f"{meta['footer']}  ·  Powered by Gaply  ·  "
                               f"Pagina {doc.page}")
        canv.restoreState()

    doc = BaseDocTemplate(out_path, pagesize=A4, leftMargin=M, rightMargin=M,
                          topMargin=28 * mm, bottomMargin=18 * mm)
    frame = Frame(M, 18 * mm, PAGE_W - 2 * M, PAGE_H - 46 * mm, id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=header_footer)])

    body = ParagraphStyle("body", fontName="Helvetica", fontSize=9.5, leading=13.5,
                          textColor=DARK, spaceAfter=5)
    h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=14, leading=17,
                        textColor=DARK, spaceBefore=10, spaceAfter=5)
    h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=10.5, leading=13,
                        textColor=SIGN, spaceBefore=7, spaceAfter=3)
    tcell = ParagraphStyle("tcell", fontName="Helvetica", fontSize=8.8, leading=11.5,
                           textColor=DARK)
    tcellw = ParagraphStyle("tcellw", parent=tcell, textColor=white,
                            fontName="Helvetica-Bold")
    bullet = ParagraphStyle("bullet", parent=body, leftIndent=10, bulletIndent=2,
                            spaceAfter=3)

    def P(s, st=tcell):
        return Paragraph(s, st)

    def base_table_style(extra=None):
        st = [("BACKGROUND", (0, 0), (-1, 0), DARK),
              ("GRID", (0, 0), (-1, -1), 0.5, LINE),
              ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
              ("LEFTPADDING", (0, 0), (-1, -1), 6),
              ("RIGHTPADDING", (0, 0), (-1, -1), 6),
              ("TOPPADDING", (0, 0), (-1, -1), 4),
              ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]
        return TableStyle(st + (extra or []))

    story = []

    # Titelblok
    t = Table([
        [P(f'<font color="{prim_hex}" size="9"><b>OFFERTE</b></font>')],
        [P(f'<font color="#FFFFFF" size="17"><b>{meta["titel"]}</b></font>')],
        [P(f'<font color="#C9C9D4" size="9.5"><i>{meta["ondertitel"]}</i></font>')],
    ], colWidths=[PAGE_W - 2 * M - 16])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), DARK),
        ("LEFTPADDING", (0, 0), (-1, -1), 14), ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (0, 0), 12), ("BOTTOMPADDING", (-1, -1), (-1, -1), 12),
        ("TOPPADDING", (0, 1), (0, 2), 3), ("BOTTOMPADDING", (0, 0), (0, 1), 3),
    ]))
    story += [t, Spacer(1, 8)]

    def lbl(k, v):
        return P(f'<font color="{sign_hex}" size="7.5"><b>{k}</b></font><br/>'
                 f'<font size="9.5">{v}</font>')

    mt = Table([
        [lbl("AAN", meta["aan"]), lbl("T.A.V.", meta["tav"])],
        [lbl("VAN", meta["van"]), lbl("DATUM", meta["datum"])],
        [lbl("GELDIG TOT", meta["geldig_tot"]), lbl("KENMERK", meta["kenmerk"])],
    ], colWidths=[(PAGE_W - 2 * M) / 2] * 2)
    mt.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.5, LINE),
                            ("LEFTPADDING", (0, 0), (-1, -1), 8),
                            ("TOPPADDING", (0, 0), (-1, -1), 5),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    story.append(mt)

    # 1. Wat is Gaply?
    story.append(Paragraph("1. Wat is Gaply?", h1))
    for par in cfg["wat_is_gaply"]:
        story.append(Paragraph(par, body))

    # 2. Wat lost dit op?
    story.append(Paragraph(f"2. Wat lost dit op voor {cfg['klantnaam_kort']}?", h1))
    for b in cfg["wat_lost_op"]:
        story.append(Paragraph(b, bullet, bulletText="•"))

    # 3. Analyse van de website
    an = cfg["analyse"]
    story.append(Paragraph("3. Analyse van de website", h1))
    story.append(Paragraph(an["intro"], body))
    rows = [[P("Onderdeel", tcellw), P("URL's", tcellw), P("Type content", tcellw),
             P("Fit met Gaply", tcellw)]]
    extra = []
    for i, r in enumerate(an["rijen"], start=1):
        fit_stijl = r.get("fit_stijl", "")
        rows.append([P(f"<b>{r['onderdeel']}</b>"), P(str(r["urls"])),
                     P(r["type"]),
                     P(f"<b>{r['fit']}</b>" if fit_stijl == "hoog" else r["fit"])])
        if fit_stijl == "hoog":
            extra.append(("BACKGROUND", (3, i), (3, i), PRIMBG))
        elif fit_stijl == "laag":
            extra.append(("BACKGROUND", (3, i), (3, i), REDBG))
    tot = len(rows)
    rows.append([P(f"<b>Totaal</b>"), P(f"<b>{an['totaal']}</b>"), P(""), P("")])
    extra.append(("BACKGROUND", (0, tot), (-1, tot), LIGHT))
    ta = Table(rows, colWidths=[42 * mm, 15 * mm, 76 * mm, 37 * mm], repeatRows=1)
    ta.setStyle(base_table_style(extra))
    story.append(ta)

    # 4. Scope-varianten
    va = cfg["varianten"]
    story.append(Paragraph("4. Scope-varianten", h1))
    story.append(Paragraph(va["intro"], body))
    rows = [[P("Variant", tcellw), P("In scope", tcellw), P("URL's", tcellw),
             P("Wanneer kiezen", tcellw)]]
    for r in va["rijen"]:
        rows.append([P(f"<b>{r['naam']}</b>"), P(r["scope"]), P(str(r["urls"])),
                     P(r["wanneer"])])
    tb = Table(rows, colWidths=[32 * mm, 66 * mm, 17 * mm, 55 * mm], repeatRows=1)
    tb.setStyle(base_table_style([("BACKGROUND", (0, 1), (-1, 1), PRIMBG)]))
    story.append(tb)

    # 5. Aanpak
    story.append(Paragraph("5. Aanpak", h1))
    for i, sub in enumerate(cfg["aanpak"], start=1):
        story.append(KeepTogether([Paragraph(f"5.{i} {sub['kop']}", h2),
                                   Paragraph(sub["tekst"], body)]))

    # 6. Investering
    inv = cfg["investering"]
    blok = [Paragraph("6. Investering", h1), Paragraph(inv["intro"], body)]
    namen = [r["naam"] for r in va["rijen"]]
    rows = [[P("Onderdeel", tcellw)] + [P(n, tcellw) for n in namen],
            [P("<b>Eenmalige setup</b>")] +
            [P(f'<font color="#FFFFFF"><b>{v}</b></font>' if i == 0 else v)
             for i, v in enumerate(inv["setup"])],
            [P("<b>Maandelijkse licentie</b>")] +
            [P(f'<font color="#FFFFFF"><b>{v}</b></font>' if i == 0 else v)
             for i, v in enumerate(inv["maand"])],
            [P("<b>Bevat</b>")] + [P(v) for v in inv["bevat"]]]
    n = len(namen)
    cw = [38 * mm] + [(132 * mm) / n] * n
    tc = Table(rows, colWidths=cw, repeatRows=1)
    tc.setStyle(base_table_style([("BACKGROUND", (1, 1), (1, 2), PRIM),
                                  ("BACKGROUND", (1, 3), (1, 3), PRIMBG)]))
    blok.append(tc)
    story.append(KeepTogether(blok))

    # 7. Akkoord
    ak = [Paragraph("7. Akkoord", h1), Paragraph("Voor akkoord op deze offerte:", body)]
    for i, (naam, s, mnd) in enumerate(zip(namen, inv["setup"], inv["maand"])):
        kaal = naam.replace("<br/>", " ").split("(")[0].strip()
        regel = f"{kaal} – {s} setup + {mnd}"
        ak.append(Paragraph(f"<b>{regel} (aanbevolen)</b>" if i == 0 else regel,
                            bullet, bulletText="•"))
    ak.append(Spacer(1, 6))
    sig = Table([[P(f'<font color="#FFFFFF"><b>Namens {meta["aan"]}</b></font>')],
                 [P("Gekozen variant:<br/><br/>Naam:<br/><br/>Datum:<br/><br/><br/>"
                    "Handtekening")]], colWidths=[100 * mm])
    sig.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, 0), DARK),
                             ("GRID", (0, 0), (-1, -1), 0.5, LINE),
                             ("LEFTPADDING", (0, 0), (-1, -1), 8),
                             ("TOPPADDING", (0, 0), (-1, -1), 6),
                             ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    ak.append(sig)
    story.append(KeepTogether(ak))

    doc.build(story)
    print(f"Geschreven: {out_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Gebruik: python3 generate_offerte.py config.json output.pdf")
    main(sys.argv[1], sys.argv[2])
